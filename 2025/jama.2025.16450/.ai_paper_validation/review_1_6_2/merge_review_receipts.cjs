// Mechanical artifact merge only. Scientific decisions remain in specialist records.
const fs = require('fs');
const base = '.ai_paper_validation/review_1_6_2/';
const pass = process.argv[2];
if (!['1', '2'].includes(pass)) throw new Error('Pass must be 1 or 2');
const parts = [1, 2].map(i => `checkers/parts/statistical_pass_${pass}_${i}.md`);
const receipts = [1, 2].map(i => `statistics/parts/pass_${pass}_status_${i}.md`);
const status = `PASS_${pass}_COMPLETE`;
const completed = new Set();
for (const file of receipts) {
  const text = fs.readFileSync(base + file, 'utf8');
  for (const line of text.split('\n')) {
    const match = line.match(/^\|\s*(S\d{3,})\s*\|\s*(PASS_[12]_COMPLETE)\s*\|/);
    if (match && match[2] === status) completed.add(match[1]);
  }
}
let inventory = fs.readFileSync(base + 'statistics/relationship_inventory.md', 'utf8');
const ids = [...inventory.matchAll(/^## (S\d{3,})\b/gm)].map(m => m[1]);
if (ids.length !== completed.size || ids.some(id => !completed.has(id))) {
  throw new Error(`Incomplete receipt union: inventory ${ids.length}, complete ${completed.size}`);
}
inventory = inventory.replace(new RegExp(`Current pass ${pass} status: PENDING`, 'g'), `Current pass ${pass} status: ${status}`);
fs.writeFileSync(base + 'statistics/relationship_inventory.md', inventory);
fs.writeFileSync(base + `checkers/statistical_pass_${pass}.md`,
  `# Statistical pass ${pass} — complete disjoint union\n\nAll ${ids.length} relationships have explicit ${status} receipts. Fresh specialist records and individual completion receipts follow without loss.\n\n` +
  [...parts, ...receipts].map(file => fs.readFileSync(base + file, 'utf8').replaceAll('../../../../', '../../../')).join('\n\n---\n\n'));
let coverage = fs.readFileSync(base + 'coverage_manifest.md', 'utf8');
coverage = coverage.split('\n').map(line => line.startsWith(`| statistics_pass_${pass} |`) ? line.replace('| PENDING |', '| COMPLETE |') : line).join('\n');
fs.writeFileSync(base + 'coverage_manifest.md', coverage);
console.log(`Pass ${pass}: ${ids.length} explicit complete receipts merged.`);
