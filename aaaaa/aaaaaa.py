if __name__ == '__main__':
	# incializa dos matrices de 3x3, una para guardar la ficha que se ve, 
	# y otra para un valor asociado a la ficha, para un jugador sera 1, para
	# el otro 2, entoces para ver quien gano se multiplica por fila, por 
	# columna y por diagonal, si el resultado es 1 gano el primer jugador,
	# si es 8 gano el segundo, si es 0 es porque faltaba completar, si
	# es otra cosa, estan las tres fichas, pero no son del mismo jugador
	tab1 = [[float() for ind0 in range(3)] for ind1 in range(3)]
	tab2 = [[str() for ind0 in range(3)] for ind1 in range(3)]
	for i in range(1,4):
		for j in range(1,4):
			tab1[i-1][j-1] = 0
			tab2[i-1][j-1] = " "
	turnojugador1 = True
	terminado = False
	ganador = False
	cantturnos = 0
	while not terminado:
		# dibuja el tablero
		print("") # no hay forma directa de borrar la pantalla con Python estandar
		print(" ")
		print("      ||     ||     ")
		print("   ",tab2[0][0],"  ||  ",tab2[0][1],"  ||  ",tab2[0][2])
		print("     1||    2||    3")
		print(" =====++=====++======")
		print("     ||    ||     ")
		print("   ",tab2[1][0],"  ||  ",tab2[1][1],"  ||  ",tab2[1][2])
		print("     4||    5||    6")
		print(" =====++=====++======")
		print("     ||    ||     ")
		print("   ",tab2[2][0],"  ||  ",tab2[2][1],"  ||  ",tab2[2][2])
		print("     7||    8||    9")
		print(" ")
		if not ganador and cantturnos<9:
			# carga auxiliares segun a qu� jugador le toca
			if turnojugador1:
				ficha = "O"
				valor = 1
				objetivo = 1
				print("Turno del jugador 1 (X)")
			else:
				ficha = "X"
				valor = 2
				objetivo = 8
				print("Turno del jugador 2 (O)")
			# pide la posici�n para colocar la ficha y la valida
			print("Ingrese la Posici�n (1-9):")
			while True:# no hay 'repetir' en python
				pos = int(input())
				if pos<1 or pos>9:
					print("Posici�n incorrecta, ingrese nuevamente: ")
					pos = 99
				else:
					i = int((pos-1)/3)+1
					j = ((pos-1)%3)+1
					if tab1[i-1][j-1]!=0:
						pos = 99
						print("Posici�n incorrecta, ingrese nuevamente: ")
				if pos!=99: break
			# guarda la ficha en la matriz tab2 y el valor en tab1
			cantturnos = cantturnos+1
			tab1[i-1][j-1] = valor
			tab2[i-1][j-1] = ficha
			# verifica si gan�, buscando que el producto de las fichas en el tablero de Objetivo
			aux_d1 = 1
			aux_d2 = 1
			for i in range(1,4):
				aux_i = 1
				aux_j = 1
				aux_d1 = aux_d1*tab1[i-1][i-1]
				aux_d2 = aux_d2*tab1[i-1][3-i]
				for j in range(1,4):
					aux_i = aux_i*tab1[i-1][j-1]
					aux_j = aux_j*tab1[j-1][i-1]
				if aux_i==objetivo or aux_j==objetivo:
					ganador = True
			if aux_d1==objetivo or aux_d2==objetivo:
				ganador = True
			else:
				turnojugador1 = not turnojugador1
		else:
			if ganador:
				print("Ganador: ")
				if turnojugador1:
					print("Jugador 1!")
				else:
					print("Jugador 2!")
			else:
				print("Empate!")
			terminado = True

