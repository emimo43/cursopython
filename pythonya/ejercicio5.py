"""Realizar la carga del lado de un cuadrado, mostrar por pantalla el perimetro del mismo(El perimetro de un cuadrado se calcula multiplicano el valor del lado por cuatro)"""

# Solicitamos los datos al Usuario
lado = int(input("Favor ingresar el valor del lado del cuadrado: "))

# Ahora creamos una variable llamado perimetro en la cual almacenaremos el valor de la operacion

perimetro = lado * 4

# Ahora mostramos por pantalla el valor de la operacion
print(f"El valor del perimetro del cuadrado es: {perimetro}")