"""Problema:
Realizar un programa que solicite ingresar dos numeros distintos, y muestre por pantalle el mayor de ellos"""

# Solicitamos los datos al Usuario
numero1 = int(input("Favor ingresar el primer numero: "))
numero2 = int(input("Favor ingresar el segundo numero: "))

# Ahora realizamos la condicion if
if(numero1 > numero2):
    print(f"El numero {numero1} es el mayor")
else:
    print(f"El numero {numero2} es el mayor")    