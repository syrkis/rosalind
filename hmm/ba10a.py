# ba10a.py
#   compute the probability of a hidden path
# by: Noah Syrkis

# imports
from sys import stdin
from icecream import ic
import numpy as np

# reading
G = stdin.readlines()
p = G[0].strip()
T = np.array([list(map(float, row[1:].strip().split())) for row in G[-2:]])
ic(T)
M = {"A": 0, "B": 1}
prob = .5

for i in range(1, len(p)):
    s, t = p[i - 1], p[i] 
    tmp = T[M[s], M[t]]
    prob *= tmp

ic(prob)

