#!/usr/bin/env python3
"""Exact-rational finite WZ-sketch toy for the pinned paper's Appendix case identity.
Not an LCI-Test/WZ-LLM benchmark reproduction.
"""
from fractions import Fraction
from math import comb
from pathlib import Path
import argparse, csv, json, platform, sys, time

def lhs(n,m, corrupt=False):
    s=Fraction(0)
    for k in range(n+1):
        sign = 1 if (corrupt or k%2==0) else -1
        s += sign*comb(n,k)*Fraction(m,m+k)
    return s

def rhs(n,m): return Fraction(1,comb(m+n,n))
def recurrence_residual(n,m, corrupt=False):
    # Exact induction consequence of the claimed closed form.
    return lhs(n+1,m,corrupt)-Fraction(n+1,m+n+1)*lhs(n,m,corrupt)

def main():
 p=argparse.ArgumentParser(); p.add_argument('--out',required=True); p.add_argument('--max-n',type=int,default=12); p.add_argument('--max-m',type=int,default=12)
 a=p.parse_args(); out=Path(a.out); out.mkdir(parents=True,exist_ok=True); t=time.time(); rows=[]
 for n in range(a.max_n+1):
  for m in range(1,a.max_m+1):
   L,R=lhs(n,m),rhs(n,m); bad=lhs(n,m,True)
   rows.append({'n':n,'m':m,'lhs':str(L),'rhs':str(R),'exact_residual':str(L-R),'recurrence_residual':str(recurrence_residual(n,m)),'corrupt_sign_residual':str(bad-R),'pass':L==R,'control_fails':bad!=R})
 with (out/'results.csv').open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
 result={'method':'finite exact-rational WZ-sketch identity check', 'identity':'sum_k (-1)^k C(n,k) m/(m+k)=1/C(m+n,n)', 'source_location':'WZ-LLM.tex Appendix case study / MichaelZ_052 listing', 'n_range':[0,a.max_n], 'm_range':[1,a.max_m], 'cells':len(rows), 'identity_passes':sum(r['pass'] for r in rows), 'corrupt_control_fails':sum(r['control_fails'] for r in rows), 'verdict':'toy', 'limitation':'No LCI-Test data, WZ-Prover weights, Lean tactic, or baseline inference was released; this does not reproduce 34/100.'}
 (out/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
 (out/'config.json').write_text(json.dumps({'max_n':a.max_n,'max_m':a.max_m,'python':sys.version,'platform':platform.platform()},indent=2)+'\n')
 print(json.dumps(result)); print('elapsed_seconds',time.time()-t)
if __name__=='__main__': main()
