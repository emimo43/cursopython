'''
    Ejercicio 5.->
        Realizar la carga de un cuadrado, mostrar por pantalla el perimetro del mismo (El perimetro de un cuadrado se calcula multiplicando el valor del lado por cuatro)
'''

# Solicitamos los datos al Usuario, en este caso nos indican que necesitamos el valor del lado

lado = int(input("Favor ingresar el valor del lado del cuadrado: "))

# Ahora realizamos la multiplicacion de la formula que nos indican que es del valor del lado por cuatro

perimetro = lado * 4

# Ahora mostramos por pantalla el valor del perimetro

print(f"El valor del perimetro del cuadrado es: {perimetro}")