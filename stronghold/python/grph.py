from sys import stdin
data = [[line.split('\n')[0], "".join(line.split('\n')[1:])] for line in stdin.read().split('>')]
D = {entry[0]: entry[1] for entry in data}

for ki, vi in D.items():
    for kj, vj in list(D.items()):
        if ki != kj and vi[:3] == vj[-3:]:
            print(kj, ki)
