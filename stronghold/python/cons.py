from sys import stdin
data = [line.strip().split('\n') for line in stdin.read().split('>')[1:]]
data = [[d[0], "".join(d[1:])] for d in data]
P = {l: [0] * len(data[0][1]) for l in 'ACGT'}
c = ""
pp = []

for line in data:
    line = line[1]
    for i in range(len(line)):
        P[line[i]][i] += 1

for k, v in P.items():
    p = str(v).replace(',', '')[1:-1]
    pp.append(f"{k}: {p}")
     
alpha = list(P.keys())
for i in range(len(list(P.values())[0])): 
    t = ['A', 0] 
    for a in alpha:
        if P[a][i] > t[1]:
            t = [a, P[a][i]]
    c = c + t[0]

print(c)
for p in pp:
    print(p)
