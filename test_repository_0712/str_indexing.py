seq1 = "ATGTTATAG"
#      "TACAATATC"
newseq1 = seq1
newseq1 = newseq1.replace("A", "t")
newseq1 = newseq1.replace("T", "a")
newseq1 = newseq1.replace("C", "g")
newseq1 = newseq1.replace("G", "c")
newseq1 = newseq1.upper()
print(newseq1)
