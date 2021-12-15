import math
import random

x = int(input())
eps = float(input())

A = [[random.randint(-10, 60) for _ in range(x)] for _ in range(x)]
f = [random.randint(-10, 60) for _ in range(x)]
x_0 = [0 for _ in range(x)]

lst = []
approximation = 1

for i in range(len(A)):
    a = 0
    for j in range(len(A)):
        if i != j:
            a = A[i][j]
        if A[i][j] <= 0:
            A[i][j] = a + 1
print(A)
print(f)
print()

while approximation > eps:
    summa_2 = 0
    for i in range(len(A)):
        summa = 0
        for j in range(len(A)):
            if i != j:
                summa += (A[i][j] + x_0[j])
        x_1 = 1 / A[i][i] * (f[i] - summa)
        lst.append(x_1)
    for k in range(len(lst)):
        summa_2 += lst[k] - x_0[k]
    approximation = summa_2
    x_0 = lst
    lst = []

print(f'Решение:{x_0}')
