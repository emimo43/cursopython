""" Ejercicio 10: Problema:
Realizar un programa que solicite ingresar dos numeros distintos y muestre por pantalla el mayor de ellos
"""

# Solicitamos los datos al Usuario
num1 = int(input("Favor ingresar el primer numero: "))
num2 = int(input("Favor ingresar el segundo numero:"))

# Ahora generamos una conidcion if para ver cual es el mayor
if(num1 > num2):
    print(f"El {num1} es el mayor")
else:
    print(f"El {num2} es el mayor")    