import numpy
import copy as iouweriwehjr
from copy import deepcopy as copy

def gauth():
	def find_delta(A):
		B = []

		deltax = [];
		
		for i in range(order):
			B.append(A[i][-1])
			A[i] = A[i][:-1]
		for i in range(3):
			delta = copy(A)
			for j in range(3):
				delta[j][i] = B[j]
			deltax.append(delta[0][0] * delta[1][1] * delta[2][2] + delta[0][1] * delta[1][2] * delta[2][0] + delta[1][0] * delta[2][1] * delta[0][2] - delta[0][2] * delta[1][1] * delta[2][0] - delta[0][1] * delta[1][0] * delta[2][2] - delta[0][0] * delta[1][2] * delta[2][1])
		return deltax
	order = int(input("порядок матрицы: ")) 

	A = [] 
	Xes = []

	for i in range(order): 
		A.append(list(map(float, input(f'А{str(i)} + B{str(i)}: ').split())))

	for i in range(order-1):
		
		multiplier = A[i][i] 

		try:
			for j in range(order+1):
				A[i][j] = A[i][j] / multiplier 
		
		except ZeroDivisionError:
			deltax = find_delta(A)
			if not 0 in deltax:
				print('Решений нет, жуй Дискриминант')
			else: 
				print('Решений бесчисленное множество, жуй оооооооооочень много введите')
			raise SystemExit;
		
		for j in range(order - 1 - i):
			
			tempmultiplier = A[j + 1 + i][i]

			for jj in range(order + 1):
				A[j + 1 + i][jj] = A[j + 1 + i][jj] - A[i][jj] * tempmultiplier

	for i in range(order):
		print(A[i])

	for i in range(order):
		Xes.append((A[-i - 1][-1] * 2 - sum(A[-i - 1]) + A[-i - 1][-i - 2]) / A[-i - 1][-i - 2])

		for j in range(order):
			A[j][-i - 2] = A[j][-i - 2] * Xes[-1]

	Xes = Xes[::-1]
	print(Xes)
if __name__ == '__main__':
	gauth()