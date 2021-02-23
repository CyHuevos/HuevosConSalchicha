# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


# Lee los tres lados de un triangulo rectangulo, determina 
# si corresponden (por Pitargoras) y en caso afirmativo 
# calcula el area
if __name__ == '__main__':
	# cargar datos
	print("Ingrese el lado 1:")
	l1 = input()
	print("Ingrese el lado 2:")
	l2 = input()
	print("Ingrese el lado 3:")
	l3 = input()
	# encontrar la hipotenusa (mayor lado)
	if l1>l2:
		cat1 = l2
		if l1>l3:
			hip = l1
			cat2 = l3
		else:
			hip = l3
			cat2 = l1
	else:
		cat1 = l1
		if l2>l3:
			hip = l2
			cat2 = l3
		else:
			hip = l3
			cat2 = l2
	# ver si cumple con Pitagoras
	if hip**2==cat1**2+cat2**2:
		# calcualar area
		area = (cat1*cat2)/2
		print("El area es: ",area)
	else:
		print("No es un triangulo rectangulo.")

