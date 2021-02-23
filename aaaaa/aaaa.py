from random import randint
if __name__ == '__main__':
	intentos = 10
	num_secreto = randint(0,99)+1
	print("Adivine el numero (de 1 a 100):")
	num_ingresado = input()
	while num_secreto!=num_ingresado and intentos>1:
		if int(num_secreto) > int(num_ingresado):
			print("Muy bajo")
		else:
			print("Muy alto")
		intentos = intentos-1
		print("Le quedan ",intentos," intentos:")
		num_ingresado = float(input())
	if num_secreto==num_ingresado:
		print("Exacto! Usted adivino en ",11-intentos," intentos.")
	else:
		print("El numero era: ",num_secreto)

