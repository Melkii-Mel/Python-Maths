from random import randint
n = int(input("размерность матрицы: "))
a = [[randint(-10, 11) for _ in range(n)] for _ in range(n)]
print('\n'.join(map(lambda x: ' '.join(map(lambda y: '%3.f'%y, x)), a)))