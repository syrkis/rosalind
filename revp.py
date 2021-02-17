from sys import stdin
_ = stdin.readline()
data = stdin.read().strip().replace('\n', '')

def palind(s, c):
    return True if s == c and len(s) >= 4 else False
     
def comple(s):
    D = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
    c = []
    for i in range(len(s)):
        c.append(D[s[i]])  
    return "".join(c[::-1])
     
for i in range(len(data)):
    for j in range(4, 13):
        s = data[i:i+j]
        c = comple(s)
        if palind(s, c) and len(s) == len(c) == j:
            print(i + 1, j)
