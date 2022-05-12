def fact(n):
    if n == 2:
        return 2
    return n * fact(n-1)

def pper(n, k):
    return (factorial(n) / factorial(n - k)) % 1_000_000

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
      
print(pper(98, 8))
