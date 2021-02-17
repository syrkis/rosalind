from sys import stdin
data = [[entry.strip()[:13], entry.strip()[14:].replace('\n', '')] for entry in stdin.read().split('>')[1:]]
print(data)
