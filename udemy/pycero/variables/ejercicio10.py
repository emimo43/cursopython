"""Solicitar valores al Usuario para hacer una operacion simple"""

# Solicitamos los datos al Usuario
print("Deme un valor 1:")
a = input()
print("Deme un valor 2:")
b = input()

# Generamos una variable llamada c, la cual contendra la suma de estos datos, antes debemos castear estas variables, como vienen como string
c = int(a) + int(b)
# Mostraremos por consola con los dos tipos de impresion con su concatenacion correspondiente
print("La suma de los valores es:",c) # Primera forma
print(f"La suma de los valores es:{c}")