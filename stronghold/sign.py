n = 4

l = [i for i in range(-n, n + 1) if i != 0]
P = []

def sign(pots, path):
    if len(path) == n:
        P.append(path)
    else:
        for pot in pots:
            n_pots = [p for p in pots if p != pot and p + pot != 0]
            n_path = path[:]; n_path.append(pot)
            sign(n_pots, n_path)

sign(l, [])
print(len(P))
for p in P:
    print(f"{str(p).replace(',', '')[1:-1]}")
