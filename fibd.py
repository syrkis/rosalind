from sys import stdin
n, m = map(int, stdin.readline().strip().split())

l = [0 for _ in range(m)]
l.append(1)

def fibd(l, n, m):
    if n == 0:
        return l
    l.append(sum(l[-m:-1]))
    return fibd(l, n-1, m)

out = fibd(l, n - 1, m)
print(sum(out[-m:]))
