from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import formulas,time
from openpyxl import load_workbook
from build_v_2_3_1 import HERE
p=HERE/'staging/human_adjudication_v_2_3_1_2019_R_A.xlsx'
m=formulas.ExcelModel().loads(str(p)).finish()
node=lambda s,c:f"'[{p.name}]{s.upper()}'!{c}"
s='C_jama.2019.10517'
inputs=[node('Setup','B2')]+[node(s,c+'2') for c in 'ADE FHIJKLR'.replace(' ','')]+[node('Decisions','D2')]
outputs=[node(s,'G2'),node('Decisions','G2'),node('Decisions','H2')]+[node('Decisions',c+'2') for c in 'MNOPQR']
f=m.compile(inputs,outputs)
vals=['TEST','2019::jama.2019.10517::C001','retain','statistical_results','primary_done','confirmed_issue','substantive','','','','note','S_W']
t=time.time();print('nodes',inputs)
for ans in f(*vals):print(ans.value)
print('seconds',time.time()-t)
