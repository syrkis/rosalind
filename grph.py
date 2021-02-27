from sys import stdin
data = [[entry.strip()[:13], entry.strip()[14:].replace('\n', '')] for entry in stdin.read().split('>')[1:]]


def suffix(s, t, k):
    if s[:k] in t[1:]:
        return True

A = set()

for i in range(len(data)):
    for j in range(len(data)):
        if i != j and suffix(data[i][1], data[j][1], 3):
            if int(data[i][0][-4:]) < int(data[j][0][-4:]):
                mi = data[i][0]
                ma = data[j][0]
            else:
                mi = data[j][0]
                ma = data[i][0]
            A.add(f"{mi} {ma}")

                
for l in list(A):
    print(l)
