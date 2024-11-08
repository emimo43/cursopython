'''
    Ejercicio 5.- Realizar la carga del lado de un cuadrado, mostrar por pantalla el perimetro del mismo (El perimetro de un cuadrado se calcula multiplicando el valor del lado por cuatro)
'''
# Lo primero es solicitar el lado del cuadrado al Usuario
lado = int(input("Favor ingresar el lado del cuadrado: "))

# Ahora realizamos la formula para calcular el perimetro
perimetro = lado * 4

# Ahora mostramos por consola el resultado
print(f"El perimetro del cuadrado es: {perimetro}")