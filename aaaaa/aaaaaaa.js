function promedio() {
	var acum, dato, i, n, prom;
	document.write("Ingrese la cantidad de datos:",'<BR/>');
	n = Number(prompt());
	acum = 0;
	for (i=1;i<=n;i++) {
		document.write("Ingrese el dato ",i,":",'<BR/>');
		dato = Number(prompt());
		acum = acum+dato;
	}
	prom = acum/n;
	document.write("El promedio es: ",prom,'<BR/>');
}