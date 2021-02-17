from sys import stdin
n, m = map(int, stdin.read().strip().split())

seq = [0] * m
seq.append(1)

for i in range(n):
    seq.append(seq[-2] + seq[-1])
    seq[-1] -= seq[i - m - 1]

print(seq)
