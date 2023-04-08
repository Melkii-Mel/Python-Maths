import math
from math import acos, pi

def trigonometric_complex(a, b, ifexp = 0, unb = 0):
	def quartercount(a, b):
		if a >= 0 and b >= 0:
			return 1
		if a < 0 and b >= 0:
			return 2
		if a < 0 and b < 0:
			return 3
		if a >= 0 and b < 0:
			return 4
		raise NameError("Четверть не определена");


	if ifexp == 0:
		r = (a ** 2 + b ** 2 - unb ** 2) ** 0.5
		if b != 0 and a != 0:
			quarter = quartercount(a, b)
		if b == 0 and a != 0:
			quarter = quartercount(a, b+0.01)
		if b != 0 and a == 0:
			quarter = quartercount(a+0.01, b)
		if b == 0 and a == 0:
			quarter = quartercount(a+0.01, b+0.01)
		if quarter == 1 or quarter == 3:
			phi = round(acos(abs(a)/r)/pi, 4) + (quarter - 1)/2
		elif quarter == 2 or quarter == 4:
			phi = round(acos((1 - (abs(a)/r) ** 2) ** 0.5)/pi, 4) + (quarter - 1)/2 
	else:
		r = round(a, 3)
		phi = round(b, 3)
	print(f'\nТригонометрическая запись комплексного числа: \nZ = {r}(sin({phi}Pi) + i*cos({phi}Pi))')
	return(r, phi)
def exponential_complex(r, phi):
	print(f'\nПоказательная запись комплексного числа: \nZ = {r}e^{phi}Pi*i')
def algebraic_complex(r, phi):
	a = round(r * math.cos(phi * pi), 3)
	b = round(r * math.sin(phi * pi), 3)
	summ = '+'
	if b != abs(b):
		b, summ = abs(b), '-'
	print(f'\nАлгебраическая запись комплексного числа: \nZ = {a} {summ} {b}i')
def algebraic_input(a = ''):
	#a = input("Алгебраическая запись комплексного числа: Z = ")
	summ = '+'
	susm = 1 if a[0] == '-' else 0
	if susm == 1: a = a[1:]
	summ = '-' if not summ in a else summ
	unb = 0
	try:
		a, b = map(str, a.split(summ))
	except ValueError:
		if a.find('i') != -1:
			b = a
			a = '0'
		else:
			b = '2';
			unb = 2;
	b = b.replace('i', '')
	a = eval(a)
	b = eval(b)
	b = -b if summ == '-' else b
	a = -a if susm == 1 else a
	#print(a, b)
	a = trigonometric_complex(a, b, 0, unb)
	exponential_complex(a[0], a[1])
def trigonometric_input(a = ''):
	try:
		r = eval(a[:a.find('(')])
	except TypeError:
		r = float(a[:a.find('(')])
	phi = str(a[a.find('cos') + len('cos'):a.find('+')])
	phi = eval(phi.replace('pi', ''))
	exponential_complex(r, phi)
	algebraic_complex(r, phi)
def exponential_input(a = ''):
	try:
		r = eval(a[:a.find('e')])
	except TypeError:
		r = float(a[:a.find('e')])
	phi	= str(a[a.find('e') + 2:a.find('p')])
	phi = eval(phi.replace('pi', ''))
	trigonometric_complex(r, phi, 1)
	algebraic_complex(r, phi)

def main():
	inpup = input("Алгебраическая/Показательная/Тригонометрическая запись комплексного числа \nZ = ")
	if inpup.find('e') != -1:
		exponential_input(inpup)
	elif inpup.find('cos') != -1:
		trigonometric_input(inpup)
	else:
		algebraic_input(inpup)

if __name__ == '__main__':
	while True:
		main()