# Archivo suma.py
#creamos la variable suma
"""suma = 2 + 3
print(suma) # mostramos por pantalla el resultado numero 5"""

"""# Ejemplo de una lista en varias lineas
a = [1,2,7,
     3,8,4,
     9]
# Ahora mostraremos por consola la lista
print(a)"""

# Ejemplo de funciones para ver la identacion
def suma_numeros(numeros): # Bloque 1
    suma = 0 # Bloque 2
    for n in numeros: # Bloque 2
        suma += n #Bloque 3
        print(suma) # Bloque 3
        return suma # Bloque 2