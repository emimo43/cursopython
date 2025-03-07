# En esta clase veremos el ingreso de datos por consola con la funcion input

# Problema: Hallar la superficie de un cuadraro conociendo el valor de un lado
# La formula es: superficie = lado * lado

# Solicitamos los datos al Usuario
# Con la funcion int() convertimos el str en entero, y con input() ingresamos por consola
lado = int(input("Favor ingrese el valor del lado: "))
# Creamos la variable superficie donde realizamos el calulo, y ese resultado lo ingresamos en la variable
superficie = lado * lado
# Ahora mediante la funcion print mostramos por consola el resultado
print(f"La superficie del cuadrado es: {superficie} ")