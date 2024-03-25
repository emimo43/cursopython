'''
    Ejercicio 2:
    Problema: Hallar la superficie de un cuadrado conociendo el valor de un lado
    La formula es superficie = lado * lado
'''
# Primero solicitamos los datos al Usuario, creo una variable de tipo int

lado = int(input("Favor ingresar el valor del lado del cuadrado: "))

# Ahora creamos la variable superficie
superficie = lado * lado

# Ahora mostramos por consola el resultado
print(f"El valor del lado del cuadrado es: {superficie}")