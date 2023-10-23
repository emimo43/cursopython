"""Ejercicio 11: Realizar un programa que solicite la carga por teclado de dos numeros, si el primero es mayor al segundo informar su suma y diferencia, en caso contrario, informar el producto y la division del primero respecto al segundo"""

# En primer lugar solicitamos los datos al Usuario
num1 = int(input("Favor ingrese el primer numero: "))
num2 = int(input("Favor ingrese el segundo numero: "))

# Ahora realizamos la condicion IF para ver el flujo de la solicitud que nos piden
if(num1 > num2):
    suma = num1 + num2
    resta = num1 - num2
    print(f"La suma de ambos numeros es: {suma}")
    print(f"La resta de ambos numeros es: {resta}")

else:
    producto = num1 * num2
    division = num1 / num2
    divisionEntera = num1 // num2

    print(f"La Multiplicacion de ambos numeros es: {producto}")
    print(f"La division de ambos numeros es: {division}")
    print(f"La division entera de ambos numeros es: {divisionEntera}")    