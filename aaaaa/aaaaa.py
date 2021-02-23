# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from time import sleep

if __name__ == '__main__':
	cohete = [str() for ind0 in range(9)]
	cohete[0] = "   /|\\   "
	cohete[1] = "   |B|   "
	cohete[2] = "   |O|   "
	cohete[3] = "   |M|   "
	cohete[4] = "   |B|   "
	cohete[5] = "  //|\\\\  "
	cohete[6] = " ******* "
	cohete[7] = "* * * * *"
	cohete[8] = " * * * * "
	# primero se muestra la primer parte del dibujo y la cuenta regresiva
	for i in range(1,12):
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		for j in range(1,16):
			print("")
		for j in range(1,7):
			print(cohete[j-1])
		print("")
		print("Lanzamiento en ",11-i)
		sleep(1)
	# despues se muestra el dibujo completo y cada vez mas arriba
	for i in range(1,16):
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		for j in range(i,16):
			print("")
		for j in range(1,9):
			print(cohete[j-1])
		if i>1:
			print(" * * * * ")
		sleep(1/i)
	# finalmente se va modificando el dibujo para hacer la explosion
	# estado tiene un entero que dice en que parte de la explosion va cada linea del dibujo
	estado = [float() for ind0 in range(6)]
	estado[0] = 3
	estado[1] = 2
	estado[2] = 1
	estado[3] = 2
	estado[4] = 3
	estado[5] = 4
	for i in range(1,11):
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		for j in range(1,7):
			estado[j-1] = estado[j-1]-1
			if estado[j-1]==0:
				cohete[j-1] = "    +    "
			elif estado[j-1]==-1 or estado[j-1]==-5:
				cohete[j-1] = "   +X+   "
			elif estado[j-1]==-2 or estado[j-1]==-4:
				cohete[j-1] = "  +XXX+  "
			elif estado[j-1]==-3:
				cohete[j-1] = " +XXXXX+ "
			elif estado[j-1]==-6:
				cohete[j-1] = "         "
			print(cohete[j-1])
		sleep(.2)

