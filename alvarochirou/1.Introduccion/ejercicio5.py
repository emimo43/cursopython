"""Ejercicio 5:
Realizar la carga del lado de un cuadrado, mostrar por pantalla el perimetro del mismo(El perimetro de un cuadrado se calcula multiplicando el valor del lado por cuatro)"""

# Solicitamos los datos al Usuario
lado = int(input("Favor ingresar el valor del lado del cuadrado: "))

# Ahora realizamos el calculo del perimetro para luego mostrarlo por pantalla
perimetro = lado * 4

print(f"El valor del perimetro del cuadrado es: {perimetro}")