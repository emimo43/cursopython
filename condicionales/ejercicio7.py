"""Realizar un programa que lea cuatro valores numericos e informar su suma y promedio"""

# Solicitamos los datos al usuario
print("Ingrese el primer numero: ")
numero1 = int(input())
print("Ingrese el segundo numero: ")
numero2 = int(input())
print("Ingrese el tercer numero: ")
numero3 = int(input())
print("Ingrese el cuarto numero: ")
numero4 = int(input())

# Ahora realizamos el calculo de la suma y su promedio
suma = numero1 + numero2 + numero3 + numero4
promedio = suma / 4

# Ahora mostramos el valor de la suma y el promedio
print(f"El valor de la suma de las cuatro notas es: {suma}")
print(f"El promedio es: {promedio}")
