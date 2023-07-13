try:
    open("noname.txt")
except FileNotFoundError:
    print("Check your input file")

print("# END")
