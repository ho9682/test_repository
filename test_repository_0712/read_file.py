seq = ""

with open("write_sample.txt") as fo:
    _ = fo.readline()
    for line in fo:
        seq += line.strip()

with open("write_result.txt", "w") as fw:
    fw.write(f"A: {seq.count('A')}\n")
    fw.write(f"C: {seq.count('C')}\n")
    fw.write(f"G: {seq.count('G')}\n")
    fw.write(f"T: {seq.count('T')}\n")
