'''
    Ejercicio 5 --> Realizar la carga del lado de un cuadraro, mostrar por pantalla el perimetro del mismo (El perimetro del cuadrado se calcula multiplicando el valor del lado por cuatro)
'''

# Solicitamos los datos al Usuario
lado = int(input("Favor ingresar el valor del lado del cuadrado: "))

# Ahora realizamos la creacion de la variable perimetro, la cual contendra la operacion que nos indica la formula
perimetro = lado * 4

# Ahora mostramos por consola el resultado de la operacion
print(f"El valor del perimetro del cuadrado es: {perimetro}")
