# En esta clase veremos la estructura repetitiva for

'''for i in range(1,6): # Aqui se indica que para i en rango de 1 a 6 se va a recorrer, pero mostrara solo del 1 al 5, debido a que el 6 es
    print(f"El indice es; {i}")'''
    
'''# Ahora con la funcion for recorreremos una lista
frutas = ['manzana', 'melon', 'platano']

# Mostramos por consola la lista
print(frutas)    

# Ahora creamos el ciclo for para recorrer la lista
for fruta in frutas: # Para la lista de frutas, la recorremos en una variable frutas
    print(fruta)'''
    
# Ahora vamos a recorrer un diccionario
diccionario = {"a":1, "b":2, "c":3}   # Esto es clave -> valor

# Ahora hacemos el ciclo for
for clave, valor in diccionario.items(): # La funcion items() permite mostrar como resultado la clave valor en pantalla dentro del ciclo for
    print("clave: ", clave, " valor: ", valor)
    
    