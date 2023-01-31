"""Problema: Realizar un programa que lea cuatro valores numericos e informar su suma y promedio"""

# Solicitamos los datos al usuario
num1 = int(input("Favor ingresar el primer numero: "))
num2 = int(input("Favor ingresar el segundo numero: "))
num3 = int(input("Favor ingresar el tercer numero: "))
num4 = int(input("Favor ingresar el cuarto numero: "))

# Ahora realizaremos las operaciones de suma y promedio
suma = num1 + num2 + num3 + num4
promedio = suma / 4

# Ahora mostramos por consola los resultados
print(f"El valor de la suma es : {suma}")
print(f"El promedio es: {promedio}")