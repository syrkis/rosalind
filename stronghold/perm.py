import sys
n = int(sys.argv[1])

def n_fact(n):
    if n == 1:
        return 1
    else:
        return n * n_fact(n-1)


print(n_fact(n))

N = [i + 1 for i in range(n)]

def brute(pots, path):
    if len(pots) == 0:
        for p in path:
            print(p, end=' ')
        print()
    for p in pots:
        n_path = path[:]
        n_path.append(p)
        n_pots = [pp for pp in pots if pp != p]
        brute(n_pots, n_path)

brute(N, [])
