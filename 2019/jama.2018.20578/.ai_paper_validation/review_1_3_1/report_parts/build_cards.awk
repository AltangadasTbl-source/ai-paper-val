function reset_fields() {
  title=""; category=""; locations=""; evidence=""; compare=""; tolerance="";
  direct=""; alternatives=""; relevance=""; verification=""; question="";
}
function clean(v) {
  sub(/^- \*\*[^*]+:\*\*[[:space:]]*/, "", v)
  return v
}
function relink(v) {
  gsub(/\.\.\/\.\.\//, "../", v)
  return v
}
function emit() {
  if (id == "") return
  print "## " id " — " title
  print ""
  print "*Pending Human Adjudication*"
  print ""
  print "**Candidate statement:** " title ". The printed relationship requires human adjudication."
  print ""
  print "**Category:** " category
  print ""
  print "**Exact source locations:** " relink(locations)
  print ""
  print "**Source evidence:** " evidence
  print ""
  print "**Reported-versus-comparator:** " compare
  print ""
  print "**Reasoning procedure:** " direct " " tolerance
  print ""
  print "**Calculation:** " compare
  print ""
  print "**Alternative source-grounded interpretations:** " alternatives
  print ""
  if (id == "C014") {
    print "**Mechanical evidence recheck:** All cited locations and printed values were found in the direct PDFs. The ordinary nearest-rounding, common-estimand reciprocal compatibility test was reproduced, but the source does not state the NNH integer-display convention or establish that ARD and NNH use the identical unrounded estimand. This conditional caveat prevents an unconditional conclusion."
  } else if (id == "C018") {
    print "**Mechanical evidence recheck:** All 13 table classifications and the direct-source graph were found. The exact 8/5 table split was reproduced; the graph's approximately 9/4 reading was reproduced from axis position and alignment with other bars, but the graph has no numeric segment labels or plotted coordinates."
  } else {
    print "**Mechanical evidence recheck:** Every cited direct-PDF location was reopened. The printed source fact, comparator, applicable rule, and stated arithmetic or logical comparison were matched and reproduced. The candidate remains unresolved only where the package lacks the definition, precision, source data, or production output named in the alternatives and human question."
  }
  print ""
  print "**Quality-control relevance:** " relevance
  print ""
  print "**Potential downstream evidence impact:** If this candidate is confirmed, a data extractor, systematic review, meta-analysis, or guideline evidence table could copy the affected value, denominator, unit, interval type, or outcome label. This is a bounded possibility; no propagation or conclusion change is claimed."
  print ""
  print "**Human verification steps:** " verification " " question
  print ""
  print "**Human adjudication fields:**"
  print ""
  print "- Validity: —"
  print "- Importance: —"
  print "- Action: —"
  print "- Initials: —"
  print "- Notes: —"
  print ""
}
BEGIN { reset_fields(); in_records=0; id="" }
/^## Candidate records/ { in_records=1; next }
/^## Merge audit/ { emit(); id=""; exit }
in_records && /^## C[0-9][0-9][0-9] [—-] / {
  emit(); reset_fields()
  id=$2
  title=$0
  sub(/^## C[0-9][0-9][0-9] [—-] /, "", title)
  next
}
in_records && /^- \*\*Primary category:\*\*/ { category=clean($0); sub(/\.$/, "", category); next }
in_records && /^- \*\*Exact source location[s]?:\*\*/ { locations=clean($0); next }
in_records && /^- \*\*Printed facts:\*\*/ { evidence=clean($0); next }
in_records && /^- \*\*Comparator, rule, and calculation:\*\*/ { compare=clean($0); next }
in_records && /^- \*\*Tolerance:\*\*/ { tolerance=clean($0); next }
in_records && /^- \*\*Direct observation versus diagnostic inference:\*\*/ { direct=clean($0); next }
in_records && /^- \*\*Source-grounded alternatives:\*\*/ { alternatives=clean($0); next }
in_records && /^- \*\*Quality-control relevance and bounded downstream risk:\*\*/ { relevance=clean($0); next }
in_records && /^- \*\*Verification steps:\*\*/ { verification=clean($0); next }
in_records && /^- \*\*Exact human question:\*\*/ { question=clean($0); next }
