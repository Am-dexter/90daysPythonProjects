def factorial(n):
    if n < 0:
        print('Cannot compute factorial of negative numbers')
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Enter a number to compute factorial:"))
print(factorial(n))
