"""Ejercicio 1: Dada la siguiente lista = [1,2,5,25,33,56,75,21,56,89,43,13,62,24].
Mostrar mediante el metodo "print" y el operador "in", si el numero 21 esta en la lista"""

lista = [1,2,5,25,33,56,75,21,56,89,43,13,62,24]
print(lista)

# Usaremos un ciclo if para ver si podemos encontrar el numero 21

numero = 21
if(numero in lista):
    print(numero)
    print("Si esta en la lista")
else:
    print("No esta en la lista")    