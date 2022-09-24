if __name__ == '__main__':
    s = input()
    aln = False
    alph = False
    ald = False
    alL = False
    alu = False
    for d in s:
        if d.isalnum(): aln = True
        if d.isalpha(): alph = True
        if d.isdigit(): ald = True
        if d.islower(): alL = True
        if d.isupper(): alu = True
    print(aln)
    print(alph)
    print(ald)
    print(alL)
    print(alu)