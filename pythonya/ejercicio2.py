'''
    Problema -> Hallar la superficie de un cuadrado conociendo el valor de un lado.
    La formula es:
    superficie = lado * lado
'''

# Lo primero que debemos hacer es solicitar los datos al Usuario
lado = int(input("Favor ingrese el valor del lado del cuadrado: "))

# Ahora generamos una variable que se llame superficie la cual contendra la operacion que necesitamos
superficie = lado * lado

# Ahora mostramos en consola el resultado de esta operacion
print(f"El valor de la superficie del cuadrado es: {superficie}")