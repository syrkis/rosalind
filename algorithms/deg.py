from collections import defaultdict

with open('../data/rosalind_deg.txt', 'r') as f:
    E = list(map(int, f.read().strip().split()))
    N = set([E[i] for i in range(0, len(E), 2)])
    print(N)

D = defaultdict(int)

for n in E:
      
    D[n] += 1

print(sorted(D.items(), key=lambda x: x[0]))
