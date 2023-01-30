"""Problema:
    Realizar la carga de dos numeros enteros por teclado e imprimir su suma y su producto."""

# Debemos solicitar ambos numeros al usuario
num1 = int(input("Favor ingresar el primer numero: "))
num2 = int(input("Favor ingresar el segundo numero: "))

# Ahora realizamos ambas operaciones, tanto la suma como el producto que es la multiplicacion
suma = num1 + num2 # Operacion suma
multiplicacion = num1 * num2 # Operacion de multiplicacion

# Ahora mostraremos ambas operaciones por consola
print(f"El resultado de la suma es: {suma}")
print(f"El resultado de la multiplicacion es: {multiplicacion}")