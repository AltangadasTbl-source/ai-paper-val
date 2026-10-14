// Mechanical synchronization of finalized timing fields; no scientific decisions.
const fs = require('fs');
const path = require('path');
const root = '.ai_paper_validation/review_1_6_2';
const statePath = path.join(root, 'run_state.md');
const reportPath = '.ai_paper_validation/final_report_1_6_2.md';
let state = fs.readFileSync(statePath, 'utf8');
let report = fs.readFileSync(reportPath, 'utf8');
const started = state.match(/^- \*\*Started UTC:\*\* (.+)$/m)[1];
const finished = new Date().toISOString().replace(/\.\d{3}Z$/, 'Z');
const elapsed = (Date.parse(finished) - Date.parse(started)) / 60000;
const upper = Number(state.match(/^- \*\*Target elapsed minutes:\*\* \d+-(\d+)$/m)[1]);
const values = {
  'Finished UTC': finished,
  'Observed elapsed minutes': elapsed.toFixed(2),
  'Target status': elapsed <= upper ? 'MET_TARGET' : 'EXCEEDED_TARGET',
  'Exceedance causes': elapsed <= upper ? 'None' : 'CUDA library setup and three corrupt-render replacements; fresh mapping of 241 source pages; sequential independent screening, recheck and audit, including repeated review of 67 excluded observations; complete six-card report assembly.'
};
for (const [label, value] of Object.entries(values)) {
  const re = new RegExp('^- \\*\\*' + label + ':\\*\\* .+$', 'm');
  if (!re.test(state)) throw new Error('Missing timing label ' + label);
  state = state.replace(re, '- **' + label + ':** ' + value);
}
state = state.replace(/^Stage:.*$/m, 'Stage: Scientific review and complete Markdown assembly finished; integrity checks, standalone HTML rendering, temporary tooling removal and final mechanical validation follow.');
const fields = ['Target basis', 'Total source units', 'Fresh-source units', 'Target elapsed minutes', 'Started UTC', 'Finished UTC', 'Observed elapsed minutes', 'Target status', 'Exceedance causes'];
for (const label of fields) {
  const re = new RegExp('^- \\*\\*' + label + ':\\*\\* .+$', 'm');
  const line = state.match(re)[0];
  if (!re.test(report)) throw new Error('Report lacks timing field ' + label);
  report = report.replace(re, line);
}
fs.writeFileSync(statePath, state);
fs.writeFileSync(reportPath, report);
process.stdout.write(JSON.stringify({finished, elapsedMinutes: elapsed.toFixed(2), status: values['Target status']}) + '\n');
