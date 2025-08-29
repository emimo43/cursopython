'''
    Ejercicio 10 .-> Problema .-> Realizar un programa que solicite ingresar dos numeros distintos, muestre por pantalla el mayor de ellos
'''

numero1 = int(input("Favor ingrese el primer numero: "))
numero2 = int(input("Favor ingrese el segundo numero: "))

# Ahora generamos la condicion if para ver cual es el numero mayor
if numero1 > numero2:
    print(f"El numero mayor es el: {numero1}")
else:
    print(f"El numero mayor es el: {numero2}")