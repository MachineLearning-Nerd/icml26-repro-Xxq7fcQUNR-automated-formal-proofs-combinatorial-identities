from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parents[1]/'src'))
from claim1_wz_identity_toy import lhs,rhs,recurrence_residual
def test_exact_identity_grid():
 for n in range(9):
  for m in range(1,9):
   assert lhs(n,m)==rhs(n,m)
   assert recurrence_residual(n,m)==0
def test_corrupt_sign_control_fails():
 assert lhs(4,3,True)!=rhs(4,3)
