"""Problema: Confeccionar un programa que permita cargar un numero entero positivo de hasta tres cifras y muestre un mensaje indicando si tiene 1,2, o 3 cifras. Mostrar un mensaje de error si el numero de cifras es mayor"""

# Solicitamos los datos al Usuario
numero = int(input("Favor ingresar un numero entero positivo: "))

# Ingresamos al ciclo
if(numero > 0):
    if(numero < 10):
        print(f"El numero {numero} es de una cifra")
    elif(numero >= 10 and numero < 100):
        print(f"El numero {numero} es de dos cifras")
    elif(numero >= 100 and numero < 1000):
        print(f"El numero {numero} es de tres cifras")
    else:
        print(f"El numero {numero} ingresado contiene mas de tres cifras")
else:
    print("El numero ingresado no es positivo")            