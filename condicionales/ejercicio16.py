"""Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el numero es positivo, negativo o nulo (es decir cero)"""

# Solicitamos los datos al usuario
numero = int(input("Favor ingrese un numero: "))

if(numero == 0):
    print(f"El numero {numero} es nulo")
else:
    if(numero > 0):
        print(f"El numero {numero} es positivo")
    elif(numero < 0):
        print(f"El numero {numero} es negativo")        