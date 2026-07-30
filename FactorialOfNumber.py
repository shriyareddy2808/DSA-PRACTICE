def factorial(n):
    fact = 1
    for c in range(1, n + 1):
        fact *= c
    return fact

n = int(input())
print(factorial(n))
