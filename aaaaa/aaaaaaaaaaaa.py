print("El menor de tres")
print("Introduce un numero")
n1=input()
print("Introduce otro numero")
n2=input()
print("Introduce el ultimo numero")
n3=input()
int(n1)
int(n2)
int(n3)
if n1<n2 and n1<n3:
    print(n1, "Es el numero menor")
elif n2<n1 and n2<n3:
    print(n2, "Es el numero menor")
elif n3<n1 and n3<n2:
    print(n3, "Es el numero menor")
else:
    print("Los numeros son iguales")