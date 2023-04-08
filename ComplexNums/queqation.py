A = [int(a) for a in input().split()]
i = 0

d = A[1] ** 2 - 4 * A[0] * A[2]
print (f"D = {d}")
if d < 0:
	d = -d
	act = -A[1] / (2 * A[0])
	actact = act
	act = '' if act == 0 else (f'{act} + ')
	print(f"x1 = {act}{d ** 0.5 / (2 * A[0])}i; x2 = {act[:-2]}-{' ' if actact != 0 else ''}{d ** 0.5 / (2 * A[0])}i")
else:
	x1 = (-A[1] + d ** 0.5) / (2 * A[0])
	x2 = (-A[1] - d ** 0.5) / (2 * A[0])

	if d != 0:
		print(f"x1 = {x1}; x2 = {x2}")
	else:
		print(f"x = {x1}")