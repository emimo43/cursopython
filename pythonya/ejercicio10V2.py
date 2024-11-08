'''
    Ejercicio 10.- Problema --> Realizar un programa que solicite al ingresar dos numeros distintos, y muestre por pantalla el mayor de ellos
'''

# Solicitamos los dos numeros al Usuario
numero1 = int(input("Favor ingrese el primer numero: "))
numero2 = int(input("Favor ingrese el segundo numero: "))

# Ahora con la condicional if veremos cual es el numero mayor
if numero1 > numero2:
    print(f"El numero mayor es: {numero1}")
else:
    print(f"El numero mayor es el: {numero2}")