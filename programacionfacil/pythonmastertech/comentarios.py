# En esta clase veremos los comentarios en Python

# Imprime en la consola el texto ¡Hola mundo!
print("¡Hola mundo!")

# print("Esta línea no se ejecutará")
print("Esta línea se ejecutará")

'''
    Dividir secciones en el código
Los comentarios también se pueden usar para dividir el código en secciones más pequeñas y legibles. Por ejemplo, si tenemos una función que es especialmente larga, se pueden utilizar comentarios para dividirla en secciones más pequeñas, y explicar lo que hace cada una. Esto hará que el código sea más fácil de leer, y de entender por parte de las personas.

En el siguiente ejemplo, la función funcion_larga(), se divide en tres secciones diferentes. Mediante el uso de comentarios se explica lo que hace cada una de ellas:
'''
'''
def funcion_larga():
	# Primera sección
	# Esta sección hace esto
	. . . 
	# Segunda sección
	# Esta sección hace esto otro
	. . . 
	# Tercera sección
	# Esta sección hace otra cosa más
	. . . 
 
 Los tres puntos (. . .) en este fragmento de código representan el código Python que pondrías en cada sección; son meramente orientativos.
 '''
 
"""
Este es un comentario
multilínea de Python.
Con él, podemos ir
escribiendo múltiples líneas.
"""

'''
Este es un comentario
multilínea de Python.
Con él, podemos ir
escribiendo múltiples líneas.
'''

# Este código imprime los números del 1 al 10
for i in range(1, 11):
	print(i)
"""
# Este código está anulado y no se ejecuta
for i in range(10, 0, -1):
	print(i)
"""

'''
Docstrings
Las docstrings normalmente se utilizan para documentar elementos del código. Elementos como módulos, clases, funciones, etc.
'''