
def squares(n):
    d = dict()
    for i in range(1, n+1):
        d[i] = i*i

    return d


print("Enter a number")
n = int(input())
print(squares(n))
