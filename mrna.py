from sys import stdin
from collections import defaultdict
with open('rna_codons.txt', 'r') as f:

    T = f.read()
T = T.split() 
D = defaultdict(int)

for i in range(int(len(T)/2)):
    t = T[i * 2 + 1]
    D[t] += 1

ps = stdin.read().strip()
tmp = 1
for p in ps:
    tmp *= D[p] 

print((tmp % 10 ** 6) * 3)
