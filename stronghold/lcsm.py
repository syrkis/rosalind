from sys import stdin


def lcsm(data, S=set()):
    if not data:
        return sorted(list(S), key= lambda x: len(x))[-1]
    n = 1000 if len(S) == 0 else max([len(e) for e in list(S)])  
    T = ngrams(S, data[0], n) 
    return lcsm(data[1:], T)
  
def ngrams(S, seq, n):
    T = set()
    for i in range(1, n):
        for e in ngram(seq, i):
            T.add(e)   
    return S.intersection(T) if len(S) != 0 else T

def ngram(seq, n):
    out = []
    for i in range(len(seq) - (n - 1)):
        out.append(seq[i:i+n+1])
    return out

data = ["".join(line.split()[1:]) for line in stdin.read().split('>')[1:]]
out = lcsm(data)
print(out)
