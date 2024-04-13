'''
    Ejercicio 5 -> Realizar la carga del lado de un cuadrado, mostrar por pantalla el perimetro del mismo (El perimetro de un cuadrado se calcula
    multiplicando el valor del lado por cuatro)
'''

# Solicitamos los datos al Usuario
lado = int(input("Favor ingresa el valor del lado del cuadrado: "))

# Generamos una variable que almacenara el valor del perimetro
perimetro = lado * 4

# Ahora mostramos por consola el resultado de la operacion del calculo del perimetro
print(f"El valor del perimetro del cuadrado es: {perimetro}")
