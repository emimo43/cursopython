"""Ejercicio 2

Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:

Te llamas: <nombre>

Tu edad es: <edad>

Eres: <sexo>
"""
# Solicitamos los datos al Usuario
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo: ")

print(f"Te llamas: {nombre}")
print(f"Tu edad es: {edad}")
print(f"Eres: {sexo}")

# Otra forma de hacerlo
print(f"Te llamas: {nombre}\nTu edad es: {edad}\nEres: {sexo}")