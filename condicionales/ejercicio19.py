"""Confeccionar un programa que lea por teclado tres numeros enteros distintos y nos muestre el mayor"""

# Solicitamos los datos al usuario
numero1 = int(input("Favor ingrese el primer numero: "))
numero2 = int(input("Favor ingrese el segundo numero: "))
numero3 = int(input("Favor ingrese el tercer numero: "))

# Ahora ingresamos al ciclo if para realizar nuestras validaciones
if(numero1 > numero2 and numero1 > numero3):
    print(f"El numero mayor es el {numero1}")
else:
    if(numero2 > numero1 and numero2 > numero3):
        print(f"El numero mayor es el {numero2}")
    elif(numero3 > numero1 and numero3 > numero2):
        print(f"El numero mayor es {numero3}")        