'''Ejercicio 1

Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, y muestre la siguiente información:

• Imprima los dos primeros caracteres.

• Imprima los tres últimos caracteres.

• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” debería imprimir rca

• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! debe imprimir !odnum aloh

• Imprima la cadena en un sentido y en sentido inverso. Ej: Si la cadena es “reflejo” imprime reflejoojelfer.

'''
cadena = "Te quiero solo como amigo"
print(cadena)
print(cadena[0 : 2]) # Aqui solo imrpimimos los dos primeros caracteres
print(cadena[ : 2]) # Esta es otra forma de hacer desde 0 hasta el 2
print(len(cadena)) # Nos muestra la cantidad de caracteres que tiene el String
print(cadena[22 : 25]) # Mostramos los 3 ultimos caracteres
print(cadena[-3 : ]) # Esta es la mejor forma de mostrar los ultimos tres caracteres, pero mi forma resulto
print(cadena[::2]) # Aqui la cadena me mostrara cada salto de dos caracteres
print(cadena[:: -1]) # Con este metodo invertimos la cadena
print(cadena + cadena[ :: -1]) # Aqui concatenando las cadenas la mostramos de forma normal e inversa