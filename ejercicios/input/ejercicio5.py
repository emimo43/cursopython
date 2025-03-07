'''
Ejercicio 5.- Realizar la carga del lado de un cuadrado, mostrar por pantalla el perimetro del mismo (El perimetro del cuadrado se calcula multiplicando el valor del lado por cuatro)
'''
# Solicitamos los datos al Usuario
lado = int(input("Favor ingrese el valor del lado: "))

# Ahora creamos una variable perimetro en la cual almacenaremos el resultado de la operacion
perimetro = lado * 4

print(f"El valor del perimetro del cuadrado es: {perimetro}")