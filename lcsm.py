from sys import stdin
data = ["".join(line.split()[1:]) for line in stdin.read().split('>')[1:]]

m = min([len(line) for line in data]) 

def lcs(S, m):
    for s in S:
        for i in range(len(s)-m):
            if 
