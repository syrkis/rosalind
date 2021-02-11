from sys import stdin
gen = [l for l in stdin.readline().strip()]
D = {l : 0 for l in [l for l in 'ACGT']}
for l in gen:
    D[l] += 1
print(D.values())

