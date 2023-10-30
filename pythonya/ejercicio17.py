"""Confeccionar un programa que permita cargar un numero entero positivo de hasta tres cifras y muestre un mensaje indicando si tiene 1,2 o 3 cifras. Mostrar un mensaje de error si el numero de cifra es mayor"""

# Solicitamos los datos al Usuario
numero = int(input("Favor ingrese un numero positivo: "))

# Generamos la condicion if
if(numero < 0):
    print(f"Error ingreso un numero negativo {numero}, favor ingrese un numero positivo")
else:
    if(numero >= 0 and numero < 10):
        print(f"El numero {numero} contiene solo una cifra")
    elif(numero >= 10 and numero < 100):
        print(f"El numero {numero} contiene dos cifras")
    elif(numero >= 100 and numero < 1000):
        print(f"EL numero {numero} contiene tres cifras")
    else:
        print("El numero contiene mas de tres cifras")