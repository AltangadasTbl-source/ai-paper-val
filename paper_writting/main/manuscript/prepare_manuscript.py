#!/usr/bin/env python3
"""Prepare compact tables and a self-contained, paste-ready XeLaTeX manuscript."""
from pathlib import Path
import csv
import re

HERE = Path(__file__).resolve().parent
ANALYSIS = HERE.parent / 'analysis'

def read_csv(name):
    with (ANALYSIS / name).open(newline='') as handle:
        return list(csv.DictReader(handle))

def row(values):
    return ' & '.join(str(v) for v in values) + r' \\'

def number(value, digits=2):
    value = float(value)
    if abs(value) < 0.5 * 10 ** (-digits):
        value = 0
    return f'{value:.{digits}f}'

def table(name, caption, label, alignment, headings, rows, note):
    lines = [r'\begin{table}[tbp]', r'\centering\small',
             r'\caption{' + caption + '}', r'\label{' + label + '}',
             r'\begin{tabular}{' + alignment + '}', r'\toprule', row(headings), r'\midrule',
             *rows, r'\bottomrule', r'\end{tabular}',
             r'\par\smallskip\begin{minipage}{0.97\linewidth}\footnotesize ' + note + r'\end{minipage}',
             r'\end{table}']
    (HERE / 'tables' / name).write_text('\n'.join(lines) + '\n')

annual = read_csv('year_summary.csv')
columns = ['year', 'papers', 'pages', 'candidates', 'retained', 'excluded']
annual_rows = [row([a[c] for c in columns]) for a in annual]
annual_rows += [r'\midrule', row(['Total', *[sum(int(a[c]) for a in annual) for c in columns[1:]]])]
table('cohort_compact.tex', 'Availability sample and final human dispositions.', 'tab:cohort', 'lrrrrr',
      ['Year', 'Papers', 'PDF pages', 'Candidates', 'Retained', 'Excluded'], annual_rows,
      r'The packages contained 188 PDFs and one supplementary Excel worksheet. Retention includes descriptive and uncertain findings; it does not imply confirmation.')

comparisons = read_csv('period_comparisons.csv')
selected = [('primary', 'count', 'Substantive statistical: count'),
            ('primary', 'any', 'Substantive statistical: any'),
            ('secondary', 'count', 'Substantive report inconsistency'),
            ('strict', 'count', 'Confirmed statistical only'),
            ('combined', 'count', 'Combined substantive report')]
comparison_rows = []
for metric, scale, label in selected:
    c = next(c for c in comparisons if c['metric'] == metric and c['scale'] == scale)
    binary = scale == 'any'
    factor, digits = (100, 1) if binary else (1, 2)
    earlier = f"{c['early_total']}/19" if binary else number(c['early_mean'])
    later = f"{c['late_total']}/25" if binary else number(c['late_mean'])
    values = [number(factor * float(c[k]), digits) for k in ['difference', 'lower', 'upper']]
    difference = f'{values[0]} ({values[1]}, {values[2]})'
    comparison_rows.append(row([label, earlier, later, difference, number(c['p'], 3)]))
table('temporal_compact.tex', 'Exploratory comparisons using exact paper-level permutation tests.', 'tab:temporal',
      r'>{\raggedright\arraybackslash}p{4.7cm}rrrr',
      ['Outcome', '2018--2019', '2024--2025', r'Difference (95\% CI)', '$P$'], comparison_rows,
      r'Count rows show mean issues per paper; the binary row shows papers with at least one issue. Differences are later minus earlier, in counts or percentage points. Intervals use 20,000 within-period paper bootstrap resamples. Permutation $P$ values are two-sided, exact, and unadjusted. The last two rows are sensitivity analyses.')

def entries(text):
    """Read the brace-delimited fields used in the supplied bibliography."""
    output = {}
    for match in re.finditer(r'@(\w+)\s*\{\s*([^,]+),', text):
        start = match.end()
        position, depth = start, 1
        while depth:
            if text[position] == '{': depth += 1
            elif text[position] == '}': depth -= 1
            position += 1
        body = text[start:position - 1]
        fields, offset = {}, 0
        while field := re.search(r'(\w+)\s*=\s*\{', body[offset:]):
            begin = offset + field.end()
            end, level = begin, 1
            while level:
                if body[end] == '{': level += 1
                elif body[end] == '}': level -= 1
                end += 1
            fields[field.group(1)] = body[begin:end - 1]
            offset = end
        output[match.group(2).strip()] = fields
    return output

def flatten(path, skip_bibliography=False, stack=()):
    path = path.resolve()
    if path in stack:
        raise ValueError(f'Cyclic input: {path}')
    text = path.read_text()
    def replace(match):
        name = match.group(1)
        if skip_bibliography and name == 'bibliography':
            return ''
        target = HERE / name
        if not target.suffix:
            target = target.with_suffix('.tex')
        return '\n% Begin embedded ' + name + '\n' + flatten(target, skip_bibliography, (*stack, path)) + '\n% End embedded ' + name + '\n'
    return re.sub(r'\\input\{([^}]+)\}', replace, text)

body = flatten(HERE / 'manuscript_source.tex', skip_bibliography=True)
keys = list(dict.fromkeys(key.strip() for group in re.findall(r'\\cite(?:p|t)?\{([^}]+)\}', body) for key in group.split(',')))
bib = entries((HERE / 'references.bib').read_text())
assert not set(keys) - set(bib), f'Missing bibliography keys: {set(keys) - set(bib)}'
bibliography = [r'% Generated from references.bib; embedded in the standalone manuscript.',
                r'\begin{thebibliography}{' + str(len(keys)) + '}']
for key in keys:
    b = bib[key]
    authors = b['author'].split(' and ')
    formatted = []
    for name in authors[:6]:
        family, given = name.split(', ', 1)
        initials = ''.join(token[0] for token in re.split(r'[\s~-]+', given) if token)
        formatted.append(f'{family} {initials}')
    if len(authors) > 6:
        formatted.append('et~al.')
    short = authors[0].split(',')[0] + ' et~al.'
    bibliography.append(r'\bibitem[' + short + '(' + b['year'] + ')]{' + key + '}')
    title = b['title'].rstrip()
    if title[-1] not in '.?!':
        title += '.'
    bibliography.append(', '.join(formatted).rstrip('.') + '. ' + title)
    if 'journal' in b:
        publication = r'\emph{' + b['journal'] + '}. ' + b['year']
        if 'volume' in b: publication += ';' + b['volume']
        if 'number' in b: publication += '(' + b['number'] + ')'
        if 'pages' in b: publication += ':' + b['pages']
        if 'note' in b: publication += '. ' + b['note']
        bibliography.append(publication.rstrip('.') + '.')
        bibliography.append(r'\href{https://doi.org/' + b['doi'] + '}{doi:' + b['doi'] + '}.')
    else:
        bibliography.append(b['howpublished'] + '. ' + b['year'] + '.')
        bibliography.append(r'\url{' + b['url'] + '}.')
    bibliography.append('')
bibliography.append(r'\end{thebibliography}')
(HERE / 'bibliography.tex').write_text('\n'.join(bibliography) + '\n')
standalone = '% !TeX program = xelatex\n% Paste this entire file into Overleaf main.tex; no external manuscript files or BibTeX run are needed.\n' + flatten(HERE / 'manuscript_source.tex')
assert not re.search(r'\\(?:input|include|includegraphics|bibliography|bibliographystyle)\s*[\[{]', standalone)
items = re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}', standalone)
assert len(items) == len(set(items)) and set(items) == set(keys)
(HERE / 'trace_q_draft.tex').write_text(standalone)
print(f'Prepared standalone trace_q_draft.tex: {len(keys)} embedded references; all inputs resolved.')
