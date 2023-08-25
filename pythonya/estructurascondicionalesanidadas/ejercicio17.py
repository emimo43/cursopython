"""Confeccionar un programa que permita cargar un numero entero positivo de hasta tres cifras y muestre un mensaje indicando si tiene 1,2 o 3 cifras. Mostrar un mensaje de error si el numero de cifras es mayor"""

# Solicitamos los datos al usuario
numero = int(input("Favor ingresar un numero entero: "))

# Iniciamos el ciclo y las validaciones correspondientes
if(numero >= 0):
    if(numero >= 0 and numero <= 9):
        print(f"El numero {numero} contiene una cifra")
    elif(numero >= 10 and numero <= 99):
        print(f"El numero {numero} contiene dos cifras")
    elif(numero >= 1000 and numero <= 999):
        print(f"El numero {numero} contiene tres cifras")
    else:
        print(f"El numero ingresado {numero} contiene mas de tres cifras")  
else:
    print(f"El numero {numero} es negativo")                

    