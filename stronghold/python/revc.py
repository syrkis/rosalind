from sys import stdin
s = stdin.readline().strip()
D = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
sc = []
for b in s:
    sc.append(D[b])
print("".join(sc[::-1]))
