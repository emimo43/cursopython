"""Problema: Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el numero es positivo, negativo o nulo(Es decir cero)"""

# Solicitamos los datos al Usuario
numero = int(input("Favor ingresar un numero entero: "))

# Ahora realizamos la estructura condicional anidada
if(numero == 0):
    print(f"El numero ingresado es {numero}, es decir nulo")
elif(numero > 0):
    print(f"El numero ingresado es {numero}, es positivo")
else:
    print(f"El numero ingresado es {numero}, es negativo")        