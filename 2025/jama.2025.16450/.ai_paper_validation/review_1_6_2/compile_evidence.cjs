// Mechanical assembly of completed specialist evidence; no candidate discovery or screening.
const fs = require('fs');
const pathTools = require('path');
const root = '.ai_paper_validation/review_1_6_2/';
function rebaseLinks(text, sourceArtifact, targetArtifact) {
  return text.replace(/(\[[^\]]+\]\()(<)?([^)>]+)(>)?(\))/g, (full, left, open, href, close, right) => {
    if (/^(?:[a-z]+:|#)/i.test(href)) return full;
    const [file, ...fragment] = href.split('#');
    const resolved = pathTools.resolve(pathTools.dirname(root + sourceArtifact), file);
    const relative = pathTools.relative(pathTools.dirname(pathTools.resolve(root + targetArtifact)), resolved);
    return left + (open || '') + relative + (fragment.length ? '#' + fragment.join('#') : '') + (close || '') + right;
  });
}
const main = ['extraction/main_numeric_01.md', 'extraction/main_statistics_01.md'];
const support = [
  'extraction/parts/protocol_results.md', 'extraction/parts/sap.md',
  'extraction/parts/manual_001_054.md', 'extraction/parts/manual_055_081.md',
  'extraction/parts/manual_082_108.md', 'extraction/parts/manual_109_162.md'
];
let aggregate = '# Complete support quantitative evidence map\n\nThis is a lossless coordinator merge of fresh specialist maps over disjoint source units. Individual visual shards are listed in coverage_manifest.md. Do not double-count the same IDs in separate aggregate and shard files. Every source page is mapped; no old scientific decisions were used.\n\n';
for (const path of support) aggregate += `\n<!-- BEGIN ${path} -->\n\n` + rebaseLinks(fs.readFileSync(root + path, 'utf8'), path, 'extraction/support_quantitative_evidence.md') + `\n<!-- END ${path} -->\n`;
fs.writeFileSync(root + 'extraction/support_quantitative_evidence.md', aggregate);
const records = new Map();
const specialistInventories = ['relationships/parts/protocol_results.md', 'statistics/parts/protocol_results.md'];
for (const path of [...specialistInventories, ...main, ...support]) {
  const lines = fs.readFileSync(root + path, 'utf8').split('\n');
  for (let i = 0; i < lines.length; i++) {
    const h = lines[i].match(/^(#{2,4})\s+([NS]\d{3,})\b/);
    if (h) {
      let j = i + 1;
      while (j < lines.length && !new RegExp('^#{1,' + h[1].length + '}\\s+').test(lines[j])) j++;
      if (!records.has(h[2])) records.set(h[2], { path, text: lines.slice(i, j).join('\n') });
    }
    const row = lines[i].match(/^\|\s*([NS]\d{3,})\s*\|/);
    if (row && !records.has(row[1])) records.set(row[1], { path, text: lines[i].replace(/\|\s*PENDING\s*\|\s*PENDING\s*\|\s*$/, '|') });
  }
}
const ids = [...records.keys()].sort((a,b) => a[0].localeCompare(b[0]) || Number(a.slice(1)) - Number(b.slice(1)));
for (const prefix of ['N','S']) {
  const selected = ids.filter(x => x.startsWith(prefix));
  let text = `# Complete ${prefix === 'N' ? 'numeric' : 'statistical'} relationship inventory\n\n${selected.length} stable mapped relationships, compiled without scientific alteration. Every record retains its specialist evidence and exact artifact locator; read the associated extraction map for definitions and footnotes. Source paths and content roles are in source_inventory.md. Initial mapper pass flags remain in the preserved extraction artifacts; the current review status fields below govern this canonical inventory.\n\n`;
  for (const id of selected) {
    const record = records.get(id);
    text += `## ${id} — mapped relationship\n\nSource mapping artifact: ${record.path}\n\n${rebaseLinks(record.text, record.path, prefix === 'N' ? 'relationships/numeric_relationship_inventory.md' : 'statistics/relationship_inventory.md')}\n\n`;
    if (prefix === 'S') text += `Current pass 1 status: PENDING. Current pass 2 status: PENDING.\n\n`;
  }
  fs.writeFileSync(root + (prefix === 'N' ? 'relationships/numeric_relationship_inventory.md' : 'statistics/relationship_inventory.md'), text);
  const shards = [];
  for (let offset = 0; offset < selected.length; offset += 120) {
    const part = selected.slice(offset, offset + 120);
    const number = shards.length + 1;
    const target = (prefix === 'N' ? 'relationships' : 'statistics') + `/parts/assigned_${prefix.toLowerCase()}_${number}.md`;
    let shard = `# Disjoint ${prefix} review shard ${number}\n\nExact scope: ${part.join(', ')}.\n\n`;
    for (const id of part) {
      const r = records.get(id);
      shard += `## ${id} — mapped relationship\n\nSource mapping artifact: ${r.path}\n\n${rebaseLinks(r.text, r.path, target)}\n\n`;
    }
    fs.writeFileSync(root + target, shard);
    shards.push({ ids: part, artifact: target });
  }
  fs.writeFileSync(root + (prefix === 'N' ? 'relationships' : 'statistics') + '/shard_assignments.json', JSON.stringify(shards, null, 2) + '\n');
  console.log(JSON.stringify({ prefix, count: selected.length, shards: shards.map(x => ({count:x.ids.length,artifact:x.artifact})) }));
}
