import assert from 'node:assert/strict';
import xml from 'xml-js';
import {normalizeUnlockedStyles} from './xlsx-compat.mjs';

// Regression: the old unlock step appended protection after extLst; Excel rejected the file.
for(const prefix of ['','x:']){
 const input=`<${prefix}styleSheet xmlns${prefix?':x':''}="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><${prefix}cellXfs count="2"><${prefix}xf fontId="2" fillId="5"><${prefix}alignment wrapText="1"/><${prefix}extLst><${prefix}ext uri="keep-extension"/></${prefix}extLst><${prefix}protection locked="1"/></${prefix}xf><${prefix}xf fontId="0"/></${prefix}cellXfs></${prefix}styleSheet>`;
 const result=normalizeUnlockedStyles(input),doc=xml.xml2js(result,{compact:false});
 const xfs=doc.elements[0].elements[0].elements;
 assert.deepEqual(xfs[0].elements.map(e=>e.name.split(':').pop()),['alignment','protection','extLst']);
 assert.equal(xfs[0].attributes.fillId,'5');
 assert.equal(xfs[0].elements[0].attributes.wrapText,'1');
 assert.equal(xfs[0].elements[1].attributes.locked,'0');
 assert.equal(xfs[0].elements[1].attributes.hidden,'0');
 assert.equal(xfs[0].elements[2].elements[0].attributes.uri,'keep-extension');
 assert.equal(xfs[1].elements[0].attributes.locked,'0');
 assert.equal(normalizeUnlockedStyles(result),result);
}
console.log('PASS namespaced/plain XML: correct style order, unlocked cells, preserved extensions and idempotent normalization.');
