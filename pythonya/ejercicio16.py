'''
    Ejercicio 16 --> Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el numero es positivo, negativo o nulo (es decir cero)
'''

# Solicitamos el numero, debe ser de tipo entero
numero = int(input("Favor ingresar un numero entero: "))

# Ahora ingresamos a la estructuta condicional para ver las opciones que nos da para tomar el resultado
if numero == 0:
    print("Nulo")
else:
    if numero > 0:
        print("Positivo")
    else:
        print("Nulo")