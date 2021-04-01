from sys import stdin
data = stdin.read()
data = [line.strip().split('\n') for line in data.split('>')][1:]
D = {}
tmp = ['tmp', 0]

for s in data:
    dna = "".join(list([s[i] for i in range(1, len(s))]))
    D[s[0]] = 0
    for l in dna:
        if l in ['G', 'C']:
            D[s[0]] += 1
    p = (D[s[0]] / (len(dna)) * 100)
    if p > tmp[1]:
        tmp = [s[0], p]
    
for d in tmp:
    print(d)
