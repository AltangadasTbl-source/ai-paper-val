// Transcribe the approved RapidOCR CLI output; preserve the raw log alongside it.
const fs = require('fs');
const [input, output] = process.argv.slice(2);
const raw = fs.readFileSync(input, 'utf8');
const line = raw.split(/\r?\n/).find(x => x.includes(' - RapidOCR - INFO: [[[['));
const strings = line ? [...line.matchAll(/(['"])((?:\\.|(?!\1)[^\\])*)\1/g)].map(x => x[2].replace(/\\n/g, '\n').replace(/\\(['"\\])/g, '$1')) : [];
const fallback = /shifted to be executed under CPUExecutionProvider|Failed to create CUDAExecutionProvider/.test(raw);
const header = `Engine: RapidOCR 1.4.4 CLI; ONNX Runtime GPU 1.28.0; requested CUDA on RTX 5070; ${fallback ? 'CPU fallback recorded in raw log' : 'CUDA requested; no CPU fallback reported'}.\nRaw log: ${input}\n\n`;
fs.writeFileSync(output, header + strings.join('\n') + '\n');
if (!line) process.stderr.write(`No OCR text detected: ${input}\n`);
