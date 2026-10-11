// Mechanical assembly only. Scientific classifications and facts come from the three recheckers.
const fs = require('fs');
const path = require('path');
const root = path.dirname(__filename);
const read = p => fs.readFileSync(path.join(root, p), 'utf8');
const write = (p, s) => fs.writeFileSync(path.join(root, p), s);
const facts = ['001','002','003'].flatMap(n => JSON.parse(read(`verification/parts/recheck_classification_${n}.json`)));
const byId = new Map(facts.map(r => [r.id, r]));
const ids = [...read('candidate_ledger.md').matchAll(/^## (C\d+) —/gm)].map(m => m[1]);
if (facts.length !== ids.length || byId.size !== ids.length || ids.some(id => !byId.has(id))) throw Error('Recheck and ledger ID sets differ');
const dispositions = {recorded_candidate:'retain',not_reproduced:'exclude',repaired_residual:'retain',record_input_error:'discuss'};
for (const r of facts) {
  if (dispositions[r.state] !== r.suggestion) throw Error(`Disposition derivation mismatch: ${r.id}`);
  const relationships = r.all.split(', ');
  const precedence = ['P_R','P_P','S_C','S_W'];
  if (!relationships.includes(r.type) || precedence.find(t => relationships.includes(t)) !== r.type) throw Error(`Relationship precedence mismatch: ${r.id}`);
  const internal = ['Measure, label, or scale inconsistency','Cross-document numeric inconsistency'];
  const domain = r.type === 'P_R' ? 'protocol_report' : r.type === 'P_P' ? 'plan_material' : internal.includes(r.category) ? 'report_internal_inconsistency' : 'statistical_results';
  if (domain !== r.domain) throw Error(`Domain derivation mismatch: ${r.id}`);
}
const compactBlocks = new Map();
let statusBrief = '# Complete cross-lane recheck status and human questions\n\nAll stable IDs are represented; full calculations and direct-source confirmation remain in evidence_recheck.md and recheck_facts.md. This is a mechanical extraction of the recheckers\' determining facts and questions.\n\n';
for (const n of ['001','002','003']) {
  const text = read(`verification/parts/recheck_facts_${n}.md`);
  const sections = text.split(/(?=^## C\d+ —)/m).slice(1);
  for (const section of sections) {
    const id = section.match(/^## (C\d+) —/)[1];
    compactBlocks.set(id, section.trim());
    const lines = section.split('\n').filter(line => /^## C\d+ —/.test(line) || line.startsWith('- Determining fact/state:') || line.startsWith('- Missing definition and human question:'));
    if (lines.length < 3) throw Error(`Missing status brief fields: ${id}`);
    statusBrief += lines.join('\n') + '\n\n';
  }
}
if (compactBlocks.size !== ids.length) throw Error('Recheck fact blocks do not cover ledger');
let ledger = read('candidate_ledger.md');
ledger = ledger.replace(/^\| (C\d+) \|.*$/gm, (line, id) => {
  const r = byId.get(id);
  return `| ${id} | ${r.category} | ${r.type} | ${r.all} | ${r.roles} | ${r.domain} | ${r.state} | ${r.suggestion} |`;
});
const fields = {'Category':'category','Relationship type':'type','All relationships':'all','Compared document roles':'roles','Review domain':'domain','Evidence state':'state','Suggested review disposition':'suggestion','Classification rationale':'rationale','Classification ambiguity':'ambiguity'};
ledger = ledger.split(/(?=^## C\d+ —)/m).map((section, i) => {
  if (i === 0) return section;
  const id = section.match(/^## (C\d+) —/)[1];
  const r = byId.get(id);
  for (const [label,key] of Object.entries(fields)) {
    const escaped = label.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    section = section.replace(new RegExp(`^\\*\\*${escaped}:\\*\\*.*$`, 'm'), `**${label}:** ${r[key]}`);
  }
  const block = compactBlocks.get(id).replace(/^## C\d+ —[^\n]*\n/, '').replaceAll('../../../../', '../../');
  return section.trimEnd() + '\n\n### Mechanical evidence recheck update\n\nThe original registration above is preserved. The following direct-source facts govern any corrected transcription or narrowed comparator interpretation.\n\n' + block + '\n\n';
}).join('');
ledger = ledger.replace('Evidence state and suggested review disposition are deliberately pending until the fresh mechanical rechecker assigns them.', 'All evidence states and mechanically derived suggestions below come from the fresh direct-source recheck; every ID remains Pending Human Adjudication.');
write('candidate_ledger.md', ledger);
write('verification/recheck_global_status.md', statusBrief.replaceAll('../../../../', '../../../'));
write('verification/recheck_classification.json', JSON.stringify(facts, null, 2) + '\n');
write('registration/final_index.json', JSON.stringify({records:ids.map(id => ({...JSON.parse(read('registration/index.json')).records.find(r => r.id === id), ...byId.get(id)}))}, null, 2) + '\n');
let index = '# Complete stable candidate index for second statistical pass\n\nEvery stable ID is present. Classification is copied mechanically from the source-confirmed recheck. Full evidence remains in candidate_ledger.md.\n\n| ID | Candidate | Category | Type | All relationships | Domain | Evidence state | Suggested review disposition |\n|---|---|---|---|---|---|---|---|\n';
const original = JSON.parse(read('registration/index.json')).records;
for (const id of ids) {
  const r = byId.get(id), o = original.find(x => x.id === id);
  index += `| ${id} | ${o.title} | ${r.category} | ${r.type} | ${r.all} | ${r.domain} | ${r.state} | ${r.suggestion} |\n`;
}
write('registration/candidate_index_for_pass2.md', index);
const counts = {};
for (const r of facts) counts[r.state] = (counts[r.state] || 0) + 1;
process.stdout.write(JSON.stringify({candidate_count:ids.length,evidence_states:counts,status_brief_chars:statusBrief.length}) + '\n');
