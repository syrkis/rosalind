from sys import stdin
import numpy as np

G = [l.strip() for l in stdin.read().split('--------')]
x = G[0]
i_t = {t: idx for idx, t in enumerate(G[2].strip().split())}
i_e = {e: idx for idx, e in enumerate(G[1].strip().split())}
T = np.array([list(map(float, l[1:].strip().split())) for l in G[3].split('\n')[1:]])
E = np.array([list(map(float, l[1:].strip().split())) for l in G[4].split('\n')[1:]])

P = []

for i in range(len(x)):    
    for j in range(len(i_t)):
        e = E[j, i_e[x[i]]]
                    

