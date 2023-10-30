"""Ejercicio 4:
Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:

Te llamas: <nombre>

Tu edad es: <edad>

Eres: <sexo>


"""
# Solicitamos los datos al Usuario
nombre = input("Favor ingrese su nombre: ")
edad = int(input("Favor ingrese su edad: "))
sexo = input("Favor ingrese su sexo: ")

# Ahora mostramos por consola
print(f"Te llamas: {nombre}\nTu edad es: {edad} años\nEres: {sexo}")