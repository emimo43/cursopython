"""Ejercicio 3:
Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas
"""

# Solicitamos los datos al Usuario
vocal = input("Favor ingresar una vocal en minuscula: ")
letra = input("Favor ingresar una letra mayuscula: ")

# Ahora convertiremos las letras como dice el enunciado
vocal = vocal.upper() # la convierto en mayuscula
letra = letra.lower() # La convierto en minuscula

# Ahora mostramos por consola
print(f"{vocal},{letra}")