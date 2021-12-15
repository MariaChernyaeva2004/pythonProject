import random


#   Функция для преобразования матрицы к ступенчатому виду
def step(matrix, coefficients, matrix_last=None, coefficients_last=None):
    if matrix_last is None:
        matrix_last = []
    if coefficients_last is None:
        coefficients_last = []
    while matrix[0][0] == 0:    #
        matrix_n = []
        coefficients_n = []
        matrix_n.extend(matrix[1:])
        matrix_n.append(matrix[0])
        coefficients_n.extend(coefficients[1:])
        coefficients_n.append(coefficients[0])
        matrix = matrix_n
        coefficients = coefficients_n

    matrix_last.append(matrix[0])
    coefficients_last.append(coefficients[0])

    if len(matrix) == 1:
        return matrix_last, coefficients_last
    matrix_new = []
    coefficients_new = []
    k = len(matrix)

    for i in range(k):
        coefficients_dop = 0
        matrix_dop = []
        num = (matrix[i][0] / matrix[0][0])
        for j in range(k):
            if i != 0:
                matrix_dop.append(matrix[i][j] - num * matrix[0][j])
        if i != 0:
            coefficients_dop = coefficients[i] - coefficients[0] * num
        if coefficients_dop != 0 or matrix_dop != []:
            matrix_new.append(matrix_dop)
            coefficients_new.append(coefficients_dop)
        else:
            matrix_new.append(matrix[0])
            coefficients_new.append(coefficients[0])
    return step([i[1:] for i in matrix_new[1:]], coefficients_new[1:]
                , matrix_last=matrix_last, coefficients_last=coefficients_last)


"""
m = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1], [1, 1, 1, 1]]
d = [1, 2, 3, 4]
"""

"""
m = [[3, 2, -5], [2, -1, 3], [1, 2, -1]]
d = [-1, 13, 9]
"""

"""
m = [[1, -1], [2, 1]]
d = [-5, -7]
"""


m = [[1, -1], [2, 1]]
d = [-5, -7]


"""
#   Генерация матриц и коэфицентов
m = []
print('Введите размеры матрицы:')
n = int(input())
for _ in range(n):
    st_in_mr = [int(random.randint(-100, 100)) for _ in range(n)]
    m.append(st_in_mr)
d = [int(random.randint(-100, 100)) for _ in range(n)]
print('Сгенирированная матрица:')
r = "{:<25}" * len(m)
for x in m:
    print(f'{r}'.format(*x))
print('Сгенирированные коэффиценты:')
print(*d, sep='\n')
"""

m, d = step(m, d)

#   Вывод измененной матрицы
print('Матрица приведённая к ступенчатому виду:')
r = "{:<25}" * len(m)
for i in range(len(m)):
    lst = list([0] * i)
    lst.extend(m[i])
    print(f'{r}'.format(*lst))

print('Её коэфиценты:')
print(*d, sep='\n')

#   Преобразование матрицы к виду с единицами
m_new, d_new = [], []
for i in range(len(m)):
    if m[i][0] != 0:
        d_new.append(d[i] / m[i][0])
        if len(m[i]) > 1:
            m_new_dop = []
            for j in range(len(m) - i - 1):
                m_new_dop.append(m[i][-1 - j] / m[i][0])
            m_new.append([1] + m_new_dop[::-1])
        else:
            m_new.append([1])
    else:
        d_new.append(0)
        m_new.append([0] * len(m))


m, d = m_new, d_new

#
print()
print('Матрица приведённая к виду с единицами:')
r = "{:<25}" * len(m)
for i in range(len(m)):
    lst = list([0] * i)
    lst.extend(m[i])
    print(f'{r}'.format(*lst))

#   Решение уравнений методом подстановки
a = [d[-1]]
for i in range(len(m) - 1):
    s = 0
    for j in range(len(a)):
        s += a[j] * m[-2 - i][-1 - j]
    a.append(d[-2 - i] - s)

#   Вывод конечного ответа
print()
print('Конечный ответ:')
print(*a[::-1], sep='\n')
