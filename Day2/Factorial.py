def factorial(n):
    if n < 0:
        raise Exception("Cannot compute factorial of negative numbers")
        # return 'Cannot compute factorial of negative numbers'
    if n == 0:
        return 1
    return n * factorial(n - 1)


n = int(input("Enter a number to compute factorial:"))
print(factorial(n))
