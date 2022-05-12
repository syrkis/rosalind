from sys import stdin

k, m, n = map(int, stdin.read().strip().split())
N = sum([k, m, n])
l = [k, m, n]
tmp = 0


for i in range(len(l)):
    p_1 = l[i] / N 
    for j in range(len(l)):
        if i == j:
            f = l[j] - 1 
        else:
            f = l[j]
        p_2 = f / (N - 1)
        if 0 in [i, j]:
            f = 1
        elif set([i, j]) == set([1, 2]):
            f = .5
        elif set([i, j]) == set([1]):
            f = .75
        else:
            f = 0
        tmp += p_1 * p_2 * f

print(tmp)
