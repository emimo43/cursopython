"""Realizar un programa que solicite la carga por teclado de dos numeros, si el primero es mayor que el segundo informar su suma y diferencia, en caso contrario informar el producto y la division del primero respecto al segundo"""

# Solicitamos los datos al usuario
num1 = int(input("Favor ingresar el primer numero: "))
num2 = int(input("Favor ingresar el segundo numero: "))

# Ahora realizaremos el ciclo if y usamos los operadores de comparacion para realizar las operaciones solicitadas
if(num1 > num2):
    # Si el numero 1 es mayor que el numero 2 creamos una variable suma y resta y mostramos por consola el resultado de ambas
    suma = num1 + num2
    resta = num1 - num2
    print(f"El numero mayor es el {num1}")
    print(f"La suma de ambos numeros es:{suma}")
    print(f"La resta de ambos numeros es:{resta}")
else:
    print(f"El numero mayor es el {num2}")
    multiplicacion = num1 * num2
    division = num1 / num2
    print(f"El resultado de la multiplicacion es:{multiplicacion}")
    print(f"El resultado de la division es:{division}")