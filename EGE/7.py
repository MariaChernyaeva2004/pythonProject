def F(n):
    if n <= 1:
        return 1
    elif n % 2 == 0 and n > 1:
        return n + F(n - 1)
    elif n % 2 != 0 and n > 1:
        return n * n + F(n - 2)


print(F(80))