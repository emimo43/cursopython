'''
    Ejercicio 7 --> Realizar un programa que lea cuatro valores numericos e informar su suma y promedio
'''

# Solicitamos los cuatro valores al Usuario
numero1 = int(input("Favor ingresar el primer valor: "))
numero2 = int(input("Favor ingresar el segundo valor: "))
numero3 = int(input("Favor ingresar el tercer valor: "))
numero4 = int(input("Favor ingresar el cuarto valor: "))

# Ahora creamos la variable suma para contabilizar este valor
suma = numero1 + numero2 + numero3 + numero4

# Ahora creamos una variable llamada promedio en la cual la variable suma la dividimos por cuatro
promedio = suma / 4

# Ahora mostramos por pantalla el resultado
print(f"El promedio de los cuatro valores es: {promedio}")
print("\nFin del Programa")