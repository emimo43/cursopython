"""Realizar la carga del lado de un cuadrado, mostrar por pantalla el perimetro del mismo (El perimetro de un cuadrado se calcula multiplicando el valor del lado por cuatro)"""

# Solicitamos los datos al usuario
print("Favor ingrese el valor del lado: ")
lado = int(input()) # Casteamos el valor del lado de str a entero

# Ahora calculamos el perimetro, que es el valor del lado por cuatro
perimetro = lado * 4

# Ahora mostramos el resultado por consola
print(f"El valor del perimetro es: {perimetro}")