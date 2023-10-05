"""Problema:
Realizar un programa que solicite ingresar dos numeros distintos y muestre por pantalla el mayor de ellos"""

# Solicitamos los datos al usuario
numero1 = int(input("Favor ingrese el primer numero: "))
numero2 = int(input("Favor ingrese el segundo numero: "))

# Ahora realizamos el ciclo de comparacion
if(numero1 > numero2):
    print(f"El {numero1} es el mayor")
else:
    print(f"El {numero2} es el mayor")    