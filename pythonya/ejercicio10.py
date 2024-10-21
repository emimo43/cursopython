'''
    Problema --> Ejercicio 10 --> Realizar un programa que solicite ingresar dos numeros distintos y muestre por pantalla el mayor de ellos
'''

# Lo primero que debemos hacer es solicitar los datos al Usuario
numero1 = int(input("Favor ingresar el primer numero entero: "))
numero2 = int(input("Favor ingresar el segundo numero entero: "))

# Ahora creamos la condicion if, para saber cual es el mayor numero
if numero1 > numero2:
    print(f"El {numero1} es el mayor")
else:
    print(f"El {numero2} es el mayor")