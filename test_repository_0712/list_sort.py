gene_expr = [3.14, 11.82, 7.44, 1.92]
codon = ["ATG", "GGC", "TGA", "CCT"]

gene_expr_sorted = sorted(gene_expr, reverse=True)
print(gene_expr_sorted)


codon_asc = sorted(codon)
codon_des = sorted(codon, reverse=True)

print(codon_asc)
print(codon_des)
