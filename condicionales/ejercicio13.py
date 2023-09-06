"""Se ingresa por teclado un numero positivo de uno o dos digitos(1..99) mostrar un mensaje indicando si el numero tiene uno o dos digitos"""

# Solicitamos los datos al usuario
numero = int(input("Favor ingrese un numero positivo: "))
# Realizamos un ciclo if para ver si el numero es positivo o no
if(numero > 0):
    print(f"El numero {numero} es positivo")
    if(numero >= 1 and numero<10):
        print(f"EL numero {numero} es de un digito")
    elif(numero >= 10 and numero<100):
        print(f"El numero {numero} es de dos digitos")
else:
    print(f"El numero {numero} es negativo")