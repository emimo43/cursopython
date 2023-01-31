"""Problema: Realizar un programa que solicite ingresar dos numeros distintos y muestre por pantalla el mayor de ellos"""

# Solicitamos los datos al usuario
num1 = int(input("Favor ingresar el primer numero: "))
num2 = int(input("Favor ingresar el segundo numero: "))

# Ahora hacemos la condicion del if
if(num1 > num2):
    print(f"El numero mayor es el {num1}")
else:
    print(f"El numero mayor es el {num2}")