from math import log10
from sys import stdin
s = stdin.readline().strip()
A = [float(n) for n in stdin.readline().strip().split()]

GC = lambda x: x/2
TA = lambda x: (1-x)/2

def calc(i):
    tmp = 1
    for l in s:
        if l in ['G', 'C']:
            tmp *= GC(A[i])
        else:
            tmp *= TA(A[i])
    print(round(log10(tmp), 5), end=' ')

for i in range(len(A)):
    calc(i)
