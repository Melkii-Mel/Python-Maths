import numpy
from copy import deepcopy as copy


A = [];
B = [];
C = [];
X = [];

for i in range(3):
	A.append(list(map(float, input('введите А'+str(i)+' ').split())))

B = list(map(float, input('введите B ').split()))

for i in range(3):
	C.append([])
	for j in range(3):
		TEMP = copy(A)
		TEMP.pop(i)
		TEMP[0].pop(j)
		TEMP[1].pop(j)
		C[i].append((TEMP[0][0] * TEMP[1][1] - TEMP[1][0] * TEMP[0][1]) * ((-1) ** (i + j)))

C = numpy.array(C)

C = C.transpose()

D = A[0][0] * A[1][1] * A[2][2] + A[0][1] * A[1][2] * A[2][0] + A[1][0] * A[2][1] * A[0][2] - A[0][2] * A[1][1] * A[2][0] - A[0][1] * A[1][0] * A[2][2] - A[0][0] * A[1][2] * A[2][1]

print("Дискриминант = " + str(D))

for i in range(3):
	for j in range(3):
		C[i][j] = float(C[i][j] * D ** (-1))
		print(C[i][j])

for i in range(3):
	X.append(B[0] * C[i][0] + B[1] * C[i][1] + B[2] * C[i][2])

for i in range(3):
	print('X'+str(i+1)+' = '+str(X[i]))