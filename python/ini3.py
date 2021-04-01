from sys import stdin
s = stdin.readline().strip()
a, b, c, d = map(int, stdin.readline().strip().split())
print(s[a:b+1], s[c:d+1])
