
from math import sqrt

if __name__ == '__main__':
	print("Ingrese el numero: ")
	num = float(input())
	print("Factorizacion: ")
	factorizar = True
	while factorizar and num>1:
		div = 0
		if num/2==int(num/2):
			print(2)
			num = num/2
		else:
			div = 1
			factor_primo = True
			while div<=sqrt(num) and factor_primo:
				div = div+2
				if num/div==int(num/div):
					factor_primo = False
			if factor_primo:
				print(num)
				factorizar = False
			else:
				print(div)
				num = num/div
				factor_primo = True

