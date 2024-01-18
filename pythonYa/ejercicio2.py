'''Ejercicio 2:
Hallar la superficie de un cuadrado conciendo el valor de un lado:
La formula es:
superficie = lado * lado'''

# Solicitamos los datos al Usuario
lado = int(input("Favor ingresar el valor del lado del cuadrado: "))
# Ahora realizamos el calculo con la variable superficie
print(f"El valor ingresado del lado del cuadrado es: {lado}")
superficie = lado * lado
# Ahora mostramos por consola el resultado
print(f"El valor de la superficie del cuadrado es: {superficie}")

# Ahora mostraremos por consola el tipo de dato de ambas variables
print(lado,type(lado))
print(superficie,type(superficie))
