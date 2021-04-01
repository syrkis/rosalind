from sys import stdin
s, t = [line.strip() for line in stdin.read().split()]
for i in range(len(s) - len(t)):
    if s[i:i+len(t)] == t:
        print(i + 1, end=' ')
print()
