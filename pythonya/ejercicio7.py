"""Realizar un programa que lea cuatro valores numericos e informar su suma y promedio"""

# Solicitamos los datos al Usuario
num1 = int(input("Favor ingresar el primer numero: "))
num2 = int(input("Favor ingesar el segundo numero: "))
num3 = int(input("Favor ingresar el tercer numero: "))
num4 = int(input("Favor ingresar el cuarto numero: "))

# Ahora creamos una variable suma y otra promedio y realizamos el calculo
suma = num1 + num2 + num3 + num4
promedio = suma / 4

# Ahora mostramos por consola el resultado de ambas operaciones
print(f"La suma de los valores es: {suma}")
print(f"El promedio es: {promedio}")