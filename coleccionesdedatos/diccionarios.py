# Los diccionarios es una coleccion de elementos estan indexados, no estan ordenados y se pueden modificar, estan por pares de claves y valor

diccionario_colores = {"red":"rojo", "blue":"azul", "yellow":"amarillo"}
print(diccionario_colores)

# Para ver el resultado de la clave lo veremos en este ejemplo
print(diccionario_colores["red"]) # Nos mostrara el valor rojo
print(diccionario_colores["yellow"]) # Nos mostrara amarillo

# Podemos hacerlo con variables
valor = diccionario_colores["yellow"]
print(valor) # Nos mostrara el valor amarillo

# Para añadir valores al diccionario, se hace de la siguiente manera
diccionario_colores["black"] = "negro"
print(diccionario_colores)

# Tambien podemos borrar valores de la siguiente manera
diccionario_colores.pop("yellow")
print(diccionario_colores)

# Otro metodo para borrar valores del diccionario, es de la siguiente manera
del(diccionario_colores["black"])
print(diccionario_colores)

# Ahora lo mostraremos con un ciclo for
for color in diccionario_colores:
    print(color) # Mostrara los valores

# Para mostrar la clave y el valor debemos usar dos variables en el bucle for   
for clave,valor in diccionario_colores.items(): #  items indica que debe mostrar la clave y el valor
    print(clave,valor) 