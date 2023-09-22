# Una lista es una coleccion de elementos que esta ordenada y se puede modificar
colores = ["rojo", "amarillo", "verde"]
print(colores)

# Posiciones de la lista comienzan en el indice 0
print(colores[0])
print(colores[1])

# Para modificar un elemento de la lista se hace de la siguiente manera
colores[1] = "azul" # Aqui indicamos que en la posicion1 cambiaremos a azul
print(colores)

# Para ver la longitud de la lista usamos la funcion len
print(len(colores))

# Para agregar un nuevo elemento a una lista usamos la funcion append()
colores.append("naranja")
print(colores)
print(colores[3])

# Para borrar un elemento de la lista usamos la funcion remove()
colores.remove("rojo")
print(colores)

# Para recorrer una lista usaremos el ciclo for de la siguiente manera
for color in colores: # color es la variable que usaremos para recorrer la lista
    print(color)

# Para borrar toda la lista usamos el metodo clear()
#print(colores.clear())    
colores = colores.clear()
print(colores)