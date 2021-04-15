from collections import defaultdict

with open('../data/rosalind_deg.txt', 'r') as f:
    data = [list(map(int, edge.split())) for edge in f.read().strip().split('\n')]

n = set([edge[0] for edge in data])

D = defaultdict(int)

for e in data:
    if e[0] in n and e[1] in n:
        D[e[0]] += 1
        D[e[1]] += 1

out = sorted(D.items(), key=lambda x: x[0])
print(out)
