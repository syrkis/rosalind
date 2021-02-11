from sys import stdin
data = stdin.read()
data = [line.strip().split('\n') for line in data.split('>')][1:]
D = {}
tmp = ['tmp', 0]

for s in data:
    D[s[0]] = 0
    for l in s[1]:
        if l in ['G', 'C']:
            D[s[0]] += 1
    p = (D[s[0]] / len(s[1])) * 100
    
    if p >= tmp[-1]:
        tmp = [s[0], p]

for e in tmp:
    print(e)
