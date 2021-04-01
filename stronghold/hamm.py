from sys import stdin
s, t = [line.strip() for line in stdin.readlines()]
d = 0
for i in range(len(s)):
    if s[i] != t[i]:
        d += 1
print(d)

