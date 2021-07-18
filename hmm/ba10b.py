from sys import stdin
import numpy as np

G = [line.strip() for line in stdin.read().split('--------')]
x = G[0]
A = {a: idx for idx, a in enumerate(G[1].split())}
p = G[2]
S = {s: idx for idx, s in enumerate(G[3].split())}
E = np.array([list(map(float, line[1:].strip().split())) for line in G[4].split('\n')[1:]])

prob = 1

for i in range(len(x)):
    prob *= E[S[p[i]], A[x[i]]]

print(prob)
