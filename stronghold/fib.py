from sys import stdin
n, k = map(int, stdin.readline().strip().split())

def fib(n, c):
    if n == 0:
        return c
    c = [c[-1], c[-1] + k * c[0]]
    return fib(n-1, c)

out = fib(n, [0, 1])[0]
print(out)
