"""Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el numero es positivo, negativo o nulo (es decir cero)"""

# Solicitamos los datos al Usuario

numero = int(input("Favor ingresar un numero: "))

# Ahora veremos la condicion IF para comprobar las condiciones

if(numero == 0):
    print(f"El numero ingresado es {numero} o sea nulo")
else:
    if(numero > 0):
        print(f"El numero ingresado {numero} es positivo")
    else:
        print(f"EL numero ingresado es {numero} negativo")