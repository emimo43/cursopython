"""Problema: Realizar un programa que solicite la carga por teclado de dos numeros, si el primero es mayor al segundo informar su suma y diferencia, en caso contrario informar el producto y la division del primero respecto al segundo"""

# Solicitamos los datos al usuario
num1 = int(input("Favor ingresar el primer numero: "))
num2 = int(input("Favor ingresar el segundo numero: "))

# Ingresamos el ciclo condicional
if(num1 > num2):
    suma = num1 + num2
    resta = num1 - num2
    print(f"El valor de la suma es: {suma}")
    print(f"El valor de la resta es: {resta}")
else:
    multiplicacion = num1 * num2
    division = num1 / num2
    print(f"El valor de la multiplicacion es: {multiplicacion}")
    print(f"El valor de la division es: {division}")    