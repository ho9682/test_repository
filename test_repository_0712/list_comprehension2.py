lst = [1, 2, 3, 4]
new_lst = [x for x in lst if x % 2 == 0]
print(new_lst)

codon = ["ATG", "GGC", "TGA", "CCT"]
codon_new = []
for seq in codon:
    if "A" not in seq:
        codon_new.append(seq)

print(codon_new)
codon_new_2 = [x for x in codon if "A" not in x]
print("codon_new_2", codon_new_2)
