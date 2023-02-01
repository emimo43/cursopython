"""Ejercicio 1

Escribir un programa que solicite al usuario un vocal en minuscula, y luego una letra en mayúsculas. El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas"""

vocal = input("Favor ingresar una vocal en minuscula: ")
letra = input("Favor ingresar una letra en mayuscula: ")

vocal = vocal.upper() # Convertimos la minuscula a mayuscula
letra = letra.lower() # Convertumos la mayuscula a minuscula

# Ahora vamos a mostrar por pantalla concatenadas las letras
print(f"{vocal} {letra}")

# Otra forma de imprimirlo
print(f"La consonante fue: {letra}\ny la vocal: {vocal}")
