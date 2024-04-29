# En esta clase veremos las listas en Python, son una coleccion de datos mutables

# Creamos una lista
lista1 = [1, 2, "A", 'a'] # Pueden contener diferentes tipos de datos

# Ahora vamos a imprimir la lista
print(lista1)
print(" ")

# Ahora veremos como imprimir un elemento de la lista, los elementos se cuentan desde el indice 0, el cual es el primer elemento de la lista
print(lista1[3]) # Aqui nos debe mostrar el dato 'a'
print("")

# Modificar un elemento de la lista
lista1[3] = 'B' # Aqui estamos indicando que en la posicion 3 se modifique el elemento al valor B
print(lista1)
print(" ")
print(type(lista1)) # Aqui veremos de que tipo de dato es lo que mostramos por consola
print(" ")

# Añadir elementos a la lista con el metodo append
lista1.append(5) # Agregamos el valor 5 a la lista, esto quedara en el final de la lista
print(lista1)
print(" ")

# Quitar elementos de una lista, con el metodo remove
lista1.remove("A") # Aqui estamos quitando el dato A
print(lista1)
print(" ")
