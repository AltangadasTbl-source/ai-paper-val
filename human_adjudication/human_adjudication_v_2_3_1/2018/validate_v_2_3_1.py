#!/usr/bin/env python3
"""2018 pre-release validation; never writes to input workbooks."""
import argparse, hashlib, json, re, sys
from pathlib import Path
from copy import deepcopy
from zipfile import ZipFile
from xml.etree import ElementTree as ET
from urllib.parse import unquote
from openpyxl import load_workbook, Workbook
from openpyxl.formula.tokenizer import Tokenizer
from openpyxl.formula.translate import Translator
from openpyxl.utils.cell import range_boundaries
from build_v_2_3_1 import HERE, BASE, SOURCE, OPTIONS, sha, hint, lookup
sys.path.insert(0,str(HERE/'tests'))
from formula_probe import Probe, parse
NS={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
REPORT={'static':[],'synthetic':[],'limitations':['No installed Excel or LibreOffice calculation/rendering engine.','Limited custom formula interpreter checks emitted formula logic; it is not proof of Excel recalculation or cached values.','Desktop Excel open/edit/save/close/reopen smoke test and visual rendering NOT RUN.']}
def check(ok,label,section='static'):
    assert ok,label
    REPORT[section].append(label)
def values(s): return list(s.values)

def static(path,role,baseline,catalog):
    w=load_workbook(path); papers=[s for s in w if s.title.startswith('C_')]
    check(len(papers)==10 and sum(s.max_row-1 for s in papers)==119,f'{role}: 10 papers / 119 rows')
    keys=[s.cell(r,1).value for s in papers for r in range(2,s.max_row+1)]
    check(len(set(keys))==119,f'{role}: unique candidate keys')
    check(keys==[s.cell(r,1).value for s in baseline if s.title.startswith('C_') for r in range(2,s.max_row+1)],f'{role}: exact candidate order')
    for name in ['Candidates','Evidence','Links','Relations']:
        check(values(w[name])==values(baseline[name]),f'{role}: {name} equals annual baseline cell-for-cell')
        rows=values(catalog[name]); idx=rows[0].index('key'); annual=[rows[0]]+[r for r in rows[1:] if str(r[idx]).startswith('2018::')]
        check(values(w[name])==annual,f'{role}: {name} equals catalog 2018 subset')
    check(w['Setup']['B2'].value is None and w['Setup']['B3'].value is None and w['Setup']['B4'].value==role,f'{role}: own role and blank identity')
    for s in papers:
        old=baseline[s.title]
        for r in range(2,s.max_row+1):
            assert [s.cell(r,c).value for c in [1,2,3,5]]==[old.cell(r,c).value for c in [1,2,3,5]]
            assert s[f'D{r}'].value is None and s[f'R{r}'].value is None and s[f'F{r}'].value=='no'
            for col in 'HIJKL': assert s[f'{col}{r}'].value==old[f'{col}{r}'].value
            assert all(s.cell(r,c).value is None for c in range(13,18))
        assert all(s.cell(1,c).value is None for c in range(13,18))
        assert s.freeze_panes==old.freeze_panes and s.max_column==18
        assert s['A1'].fill.fgColor==old['A1'].fill.fgColor
        assert len(s.data_validations.dataValidation)==8
        for dv in s.data_validations.dataValidation:
            assert len(dv.formula1)<=255 and not dv.showDropDown and dv.showErrorMessage
            assert not any(col in str(dv.sqref) for col in 'MNOPQ')
        for col in 'DEFGHIJKLR': assert s[f'{col}2'].alignment.wrap_text
    check(True,f'{role}: A–C/E preserved; blank human inputs; exact H–L defaults; 18-column layout, wrapping, freeze panes, dropdowns and empty M–Q')
    probe=Probe(w)
    check(probe.cell('Checks','B4')==0 and probe.cell('Checks','B6')==119 and probe.cell('Checks','B5')==0,f'{role}: blank-template probe shows zero ready/discuss and 119 unfinished')
    for r in range(2,121): assert probe.cell('Decisions',f'H{r}')==''
    for r in range(2,12):
        for col in 'HIJKL': assert probe.cell('Paper_counts',f'{col}{r}')==''
    check(True,f'{role}: blank-template outcomes and paper counts withheld in limited probe')
    formulas=[]; links=0
    forbidden=re.compile(r'checker|Primary_snapshot|FINAL READY|consensus|stage switch|primary_done,checker_done',re.I)
    for s in w:
        assert not s.protection.sheet
        for row in s:
            for c in row:
                assert not c.protection.locked and not c.protection.hidden
                if isinstance(c.value,str):
                    assert not forbidden.search(c.value),(s.title,c.coordinate,c.value)
                    assert ('R_B' if role=='R_A' else 'R_A') not in c.value
                    if c.data_type=='f':
                        assert len(c.value)<=8192 and '#REF!' not in c.value and '[' not in c.value
                        parse(c.value); formulas.append(c.value)
                        for t in Tokenizer(c.value).items:
                            if t.type=='OPERAND' and t.subtype=='RANGE':
                                ref=t.value
                                if '!' in ref:
                                    sh,ref=ref.rsplit('!',1); assert sh.strip("'").replace("''", "'") in w.sheetnames
                                range_boundaries(ref)
                assert c.data_type!='e'
                if c.hyperlink:
                    links+=1
                    if c.hyperlink.location:
                        sh,addr=c.hyperlink.location.split('!'); assert sh.strip("'") in w.sheetnames; range_boundaries(addr)
                    else: assert (path.parent/unquote(c.hyperlink.target.split('#')[0])).resolve().exists(),c.hyperlink.target
        for cf,rules in s.conditional_formatting._cf_rules.items():
            for rule in rules:
                for f in rule.formula: parse('='+f)
    check(not w.defined_names and not w._external_links,f'{role}: no stale names or external workbook links')
    check(w.security is None or not w.security.lockStructure,f'{role}: no structure lock')
    check(w.calculation.calcMode=='auto' and w.calculation.fullCalcOnLoad and w.calculation.forceFullCalc,f'{role}: full automatic calculation')
    with ZipFile(path) as z:
        assert not any(any(x in n.lower() for x in ['externallinks','vbaproject','connections','querytable']) for n in z.namelist())
        styles=ET.fromstring(z.read('xl/styles.xml'))
        for tag in ['cellXfs','cellStyleXfs']:
            for xf in styles.find('m:'+tag,NS):
                p=xf.find('m:protection',NS); assert p is not None and p.get('locked')=='0' and p.get('hidden')=='0'
        assert b'workbookProtection' not in z.read('xl/workbook.xml')
        for name in z.namelist():
            if name.startswith('xl/worksheets/sheet') and name.endswith('.xml'): assert b'sheetProtection' not in z.read(name)
    check(True,f'{role}: serialized cells and styles explicitly unlocked, including default/unused cells; protected ranges NONE')
    check(True,f'{role}: {len(formulas)} parsed internal formulas, maximum length {max(map(len,formulas))}; {links} valid hyperlinks; no formula error literals or obsolete workflow')
    return w

def synthetic(template, templatepath):
    w=load_workbook(templatepath); s=next(s for s in w if s.title.startswith('C_')); name=s.title; key=s['A2'].value
    base={col:s[f'{col}2'].value for col in 'DEFGHIJKLR'}
    results=[]
    def case(label,changes,status='PRIMARY READY',outcome=None,identity='TEST_REVIEWER'):
        for c,v in base.items(): s[f'{c}2']=v
        w['Setup']['B2']=identity; s['D2']='retain'; s['E2']='statistical_results'; s['H2']='confirmed_issue'; s['I2']='substantive'; s['F2']='primary_done'
        for c,v in changes.items(): s[f'{c}2']=v
        p=Probe(w); actual=p.cell(name,'G2'); check(actual==status,f'{label}: {actual}', 'synthetic')
        if outcome is not None: check(p.cell('Decisions','H2')==outcome,f'{label}: outcome {outcome or "blank"}','synthetic')
        results.append({'case':label,'inputs':changes,'identity':identity,'expected_status':status,'expected_outcome':outcome})
    case('confirmed substantive statistical',{},outcome='primary_temporal')
    case('probable substantive statistical',{'H':'probable_issue'},outcome='primary_temporal')
    case('minor statistical',{'I':'minor_presentation'},outcome='not_eligible')
    case('indeterminate issue',{'H':'indeterminate'},outcome='not_eligible')
    case('indeterminate substantiveness',{'I':'indeterminate'},outcome='not_eligible')
    case('not issue',{'H':'not_issue'},outcome='not_eligible')
    for col in 'HI':
        for value in [None,'not_applicable','pasted_invalid']:
            case(f'required {col} {value}',{col:value},'CHECK FIELDS',outcome='')
    for val in [None,'direct','possible','unlikely','unknown']: case(f'optional J {val}',{'J':val})
    for val in ['not_applicable','invalid','DIRECT']: case(f'invalid optional J {val}',{'J':val},'CHECK FIELDS')
    for domain in ['report_internal_inconsistency','plan_material']:
        changes={'E':domain,'H':None,'I':None,'K':'substantive_inconsistency'}
        case(domain,changes,outcome='secondary_temporal' if domain.startswith('report') else 'not_eligible')
        for v in [None,'not_applicable','invalid']: case(f'{domain} required K {v}',dict(changes,K=v),'CHECK FIELDS')
    for v in [None,'substantive_difference','minor_presentation','version_timing','non_inconsistency','indeterminate']:
        case(f'protocol optional {v}',{'E':'protocol_report','H':None,'I':None,'L':v},outcome='not_eligible')
    for v in ['not_applicable','invalid']: case(f'protocol invalid L {v}',{'E':'protocol_report','H':None,'I':None,'L':v},'CHECK FIELDS')
    for disposition in ['exclude','discuss']:
        case(disposition,{'D':disposition,'H':None,'I':None},outcome='not_eligible' if disposition=='exclude' else '')
        case(f'{disposition} stale answer',{'D':disposition},'CLEAR INACTIVE VALUES')
        case(f'{disposition} requires domain',{'D':disposition,'H':None,'I':None,'E':None},'CHECK FIELDS')
    for identity in [None,'   ','\t\n','\u00a0']: case(f'empty/whitespace identity {identity!r}',{},'CHECK REVIEWER ID',identity=identity)
    for col,value in [('D','invalid'),('D',None),('D','RETAIN'),('E','invalid'),('E','STATISTICAL_RESULTS')]:
        # Empty/invalid domains make literal judgments inactive, so clear them to isolate option validation.
        case(f'invalid pasted {col} {value}',{col:value,'H':None,'I':None},'CHECK FIELDS')
    case('inactive literal K',{'K':'substantive_inconsistency'},'CLEAR INACTIVE VALUES')
    case('domain change leaves literal H/I',{'E':'protocol_report'},'CLEAR INACTIVE VALUES')
    case('optional clearing',{'J':None},outcome='primary_temporal')
    case('completion reset',{'F':'no'},'PRIMARY DRAFT',outcome='')
    case('completion blank',{'F':None},'PRIMARY DRAFT',outcome='')
    for val in ['checker_done','yes','garbage','PRIMARY_DONE']: case(f'invalid completion {val}',{'F':val},'CHECK COMPLETE',outcome='')
    case('baseline ready for key tests',{})
    old=s['A2'].value
    s['A2']=None; check(Probe(w).cell(name,'G2')=='CHECK KEY','missing key rejected','synthetic')
    s['A2']=s['A3'].value; check(Probe(w).cell(name,'G2')=='CHECK KEY','duplicate key rejected','synthetic')
    s['A2']='2018::not_in_cohort::C001'; check(Probe(w).cell(name,'G2')=='CHECK KEY','unknown key rejected','synthetic')
    s['A2']=old
    # Distinct unknown-paper and missing-key effects must also reach result readiness.
    s['A2']=None
    check(Probe(w).cell('Decisions','G2')=='CHECK KEY','missing key propagates to Decisions readiness','synthetic')
    s['A2']=old
    # Full-year retained fixture uses original suggested domains and baseline option rules.
    w=load_workbook(templatepath); w['Setup']['B2']='TEST_FULL_YEAR'
    for sh in w:
        if not sh.title.startswith('C_'): continue
        for r in range(2,sh.max_row+1):
            sh[f'D{r}']='retain'; sh[f'F{r}']='primary_done'
            d=sh[f'E{r}'].value
            if d=='statistical_results': sh[f'H{r}']='confirmed_issue'; sh[f'I{r}']='substantive'
            if d in ['plan_material','report_internal_inconsistency']: sh[f'K{r}']='substantive_inconsistency'
    p=Probe(w)
    check(p.cell('Checks','B4')==119 and p.cell('Checks','B6')==0 and p.cell('Checks','B7')=='PRIMARY READY','all 119 rows ready','synthetic')
    for r in range(2,12):
        assert p.cell('Paper_counts',f'F{r}')=='yes' and p.cell('Paper_counts',f'G{r}')=='yes'
        assert sum(p.cell('Paper_counts',f'{col}{r}') for col in 'HIJKL')==p.cell('Paper_counts',f'C{r}')
    check(True,'all 10 paper totals reconcile','synthetic')
    REPORT['full_year_expected_counts']={col:sum(p.cell('Paper_counts',f'{col}{r}') for r in range(2,12)) for col in 'HIJKL'}
    for sh in w:
        for row in sh:
            for c in row:
                if c.data_type=='f': p.cell(sh.title,c.coordinate)
    check(True,'every formula evaluated in full-year synthetic copy by limited probe','synthetic')
    w['Start']['B2']='TEST ONLY — SYNTHETIC FULL YEAR; never deliver as research data'
    w.save(HERE/'tests/TEST_full_year.xlsx')
    # Preserve a complete-paper discuss case: readiness passes, counts withheld.
    s=w[name]; s['D2']='discuss'
    for col in 'HIJKL': s[f'{col}2']=None
    p=Probe(w)
    check(p.cell('Checks','B7')=='PRIMARY READY' and p.cell('Checks','B5')==1,'discuss counted; independent review remains complete','synthetic')
    check(p.cell('Decisions','H2')=='' and p.cell('Paper_counts','F2')=='yes' and p.cell('Paper_counts','G2')=='no' and p.cell('Paper_counts','H2')=='','discuss outcome blank and paper counts withheld','synthetic')
    w['Start']['B2']='TEST ONLY — SYNTHETIC DISCUSS; never deliver as research data'; w.save(HERE/'tests/TEST_discuss.xlsx')
    s['F2']='no'; p=Probe(w)
    check(p.cell('Checks','B6')==1 and p.cell('Paper_counts','F2')=='no' and p.cell('Paper_counts','H2')=='','unfinished paper counts withheld','synthetic')
    # P_R / P_P relationship precedence even if reviewer chooses a statistical domain.
    for relation,outcome in [('P_R','protocol_descriptive'),('P_P','plan_descriptive')]:
        r=next(r for r in range(2,121) if w['Decisions'][f'D{r}'].value==relation)
        key=w['Decisions'][f'C{r}'].value; sh=w['C_'+w['Decisions'][f'B{r}'].value]
        rr=next(r for r in range(2,sh.max_row+1) if sh[f'A{r}'].value==key)
        for col in 'HIJKL': sh[f'{col}{rr}']=None
        for col,v in {'D':'retain','E':'statistical_results','F':'primary_done','H':'probable_issue','I':'substantive'}.items(): sh[f'{col}{rr}']=v
        check(Probe(w).cell('Decisions',f'H{r}')==outcome,f'{relation} descriptive precedence','synthetic')
    # Whole-row permutation, translating row-relative formulas as Excel sorting does.
    w=load_workbook(HERE/'tests/TEST_full_year.xlsx'); sh=w[name]
    sh['R2']='TEST_KEY_SPECIFIC_NOTE'; oldkey=sh['A2'].value
    saved=[[c.value for c in row] for row in sh.iter_rows(min_row=2)]
    for dest,src in enumerate(reversed(range(2,sh.max_row+1)),2):
        for col,v in enumerate(saved[src-2],1):
            if isinstance(v,str) and v.startswith('='): v=Translator(v,origin=sh.cell(src,col).coordinate).translate_formula(sh.cell(dest,col).coordinate)
            sh.cell(dest,col).value=v
    p=Probe(w)
    check(p.cell('Decisions','P2')=='TEST_KEY_SPECIFIC_NOTE' and p.cell('Checks','B4')==119,'whole-row reorder preserves key mapping','synthetic')
    w.save(HERE/'tests/TEST_reordered.xlsx')
    # Single-candidate lookup/hint formula fixture; no other year source is modified or needed.
    one=Workbook(); one.remove(one.active)
    for title in ['Setup','C_one','Decisions']: one.create_sheet(title)
    one['Setup']['B2']='TEST_ONE'; sh=one['C_one']; sh.append(['key','title','location','disposition','domain','complete','hint'])
    sh.append(['2018::one::C001',None,None,'retain','protocol_report','primary_done'])
    sh['G2']=hint(2,1,1).replace('MID(A2,7,LEN(A2)-12)','"one"')
    one['Decisions']['B2']='one'; one['Decisions']['C2']='2018::one::C001'; one['Decisions']['G2']='='+lookup('C_one','G','C2',1)
    check(Probe(one).cell('Decisions','G2')=='PRIMARY READY','single-candidate INDEX/MATCH and readiness','synthetic')
    one.save(HERE/'tests/TEST_single_candidate.xlsx')
    # Independence uses separate in-memory files; modifying one must not change the other.
    untouched=values(template[name]); w[name]['D2']='exclude'
    check(values(template[name])==untouched,'mutating test copy leaves template untouched','synthetic')
    (HERE/'tests/scenarios.json').write_text(json.dumps(results,indent=2)+'\n')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--year',type=int,choices=[2018],required=True); ap.add_argument('--input-dir',default='staging'); args=ap.parse_args()
    folder=(HERE/args.input_dir).resolve(); assert folder.is_relative_to(HERE)
    baseline=load_workbook(SOURCE); catalog=load_workbook(BASE/'resources/source_catalog_v_2_1_5_3.xlsx')
    for src in json.loads((HERE/'baseline_inventory.json').read_text())['source_files']: assert sha(Path(src['path']))==src['sha256']
    check(True,'all seven source hashes unchanged and equal supplied inventory')
    ws=[]
    for role in ['R_A','R_B']: ws.append(static(folder/f'human_adjudication_v_2_3_1_2018_{role}.xlsx',role,baseline,catalog))
    for a,b in zip(ws[0],ws[1]):
        assert a.title==b.title
        for ra,rb in zip(a,b):
            for ca,cb in zip(ra,rb):
                if (a.title,ca.coordinate) in [('Setup','B4'),('Manifest','B5')]: continue
                assert ca.value==cb.value,(a.title,ca.coordinate)
    check(True,'role files have identical baseline content and blank assessments; only own role differs')
    synthetic(ws[0],folder/'human_adjudication_v_2_3_1_2018_R_A.xlsx')
    REPORT['input_dir']=str(folder); REPORT['counts']={k:len(REPORT[k]) for k in ['static','synthetic']}
    REPORT['hashes']={p.name:sha(p) for p in folder.glob('*.xlsx')}
    (HERE/f'validation_report.{folder.name}.json').write_text(json.dumps(REPORT,indent=2)+'\n')
    print(json.dumps(REPORT['counts'])); print('Excel calculation/rendering and saved/reopened smoke test: NOT RUN')
if __name__=='__main__': main()
