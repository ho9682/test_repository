import pandas as pd
from Bio.Seq import Seq

seq1 = "ATGTTATAG"
seq1_obj = Seq(seq1)
print(seq1)
print(seq1_obj.complement())
