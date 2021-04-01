from collections import defaultdict

with open('rosalind_ini6.txt', 'r') as f:
    data = f.read().strip().split()

D = defaultdict(int)
for word in data:
    D[word] += 1

for k, v in D.items():
    print(k, v)
