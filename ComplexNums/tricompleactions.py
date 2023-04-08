# -*- coding: utf8 -*-
import math
from math import *

def multiplication(z1, z2):
	phi = z1[1] + z2[1]
	r = z1[0] * z2[0]
	while phi > 2:
		phi -= 2
	while phi < -2:
		phi += 2
	print(f'Z1 * Z2 = {r}(cos{round(phi, 4)}pi + i*sin{round(phi, 4)}pi) = {round((r * cos(phi * pi)), 4)} + {round((r * sin(phi * pi)), 4)}i')
def divizion(z1, z2): #BFG
	phi = z1[1] - z2[1]
	r = z1[0] / z2[0]
	while phi > 2:
		phi -= 2
	while phi < -2:
		phi += 2
	print(f'Z1 * Z2 = {r}(cos{round(phi, 4)}pi + i*sin{round(phi, 4)}pi) = {round((r * cos(phi * pi)), 4)} + {round((r * sin(phi * pi)), 4)}i')
def exponentiation(z1, z2, whichz, power):
	z = z1 if whichz == 1 else z2
	phi = z[1] * power
	r = z[0] ** power
	while phi > 2:
		phi -= 2
	while phi < -2:
		phi += 2
	print(f'Z{whichz} ^ {power} = {r}(cos{round(phi, 4)}pi + i*sin{round(phi, 4)}pi) = {round((r * cos(phi * pi)), 4)} + {round((r * sin(phi * pi)), 4)}i')
def root(z1, z2, whichz, power):
	z = z1 if whichz == 1 else z2
	r = z[0] ** (1 / power)
	for i in range(power):
		phi = (z[1] + 2 * i) / power
		while phi > 2:
			phi -= 2
		while phi < -2:
			phi += 2
		print(f'{i}) Z sqrt {power} = {r}(cos{round(phi, 4)}pi + i*sin{round(phi, 4)}pi) = {round((r * cos(phi * pi)), 4)} + {round((r * sin(phi * pi)), 4)}i')

def inpup():
	
	def adjustment(nuber):
		z1 = input(f'Z{nuber} = ')
		try:
			r = eval(z1[:z1.find('(')])
		except TypeError:
			r = float(z1[:z1.find('(')])
		phi = str(z1[z1.find('cos') + len('cos'):z1.find('+')])
		phi = eval(phi.replace('pi', ''))
		return(r, phi)

	#action = map(str, input("Действие ( * , / , ^ , sqrt )").split())
	action = [str(a) for a in input("Действие ( * , / , ^ , sqrt ): ").split()]
	if ('*' or '/') in action:
		z1 = adjustment(1)
		z2 = adjustment(2)
	else:
		z1 = adjustment('')
		z2 = None
	if '^' in action:
		power = int(input('Степень: '))
		if ('*' or '/') in action:
			whichz = int(input('Z1 xor Z2 для возведения в степень? : '))
		else: whichz = 1
	if 'sqrt' in action:
		powerrt = int(input('Степень корня: '))
		if ('*' or '/') in action:
			whichzrt = int(input('Z1 xor Z2 для извлечения корня? : '))
		else: whichzrt = 1
	print(action)
	if '*' in action:
		multiplication(z1, z2)
	if '/' in action:
		divizion(z1, z2)
	if '^' in action:
		exponentiation(z1, z2, whichz, power)
	if 'sqrt' in action:
		root(z1, z2, whichzrt, powerrt)

def main():
	print('Алгоритм предназначен для \nвычисления произведения, частного двух комплексного числа в тригонометрической записи, \nа также возведения в степень или извлечения корня из комплексного числа. \nЗаписывать комплексные числа необходимо в общей форме:\nn(cosphipi + i*sinphipi)\nДопустима запись phi в виде выражения.\nВозможны исключения.\nВычисления могут быть неточными.')
	inpup()

if __name__ == '__main__':
	main()