# En esta clase veremos lo que son las colecciones de datos -> Conjuntos

# Creamos los conjuntos

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

# Vamos a imprimir los conjuntos
print(conjunto1)
print(conjunto2)
print(" ")

# Ahora veremos la union de los conjuntos -> Este metodo, muestra todos los elementos de ambos conjuntos, en este caso el numero 3 lo muestra solo una vez, no duplica los datos repetidos
union = conjunto1.union(conjunto2)
print(union)
print(" ")

# Ahora veremos la interseccion -> Solo muestra el dato que se repite en ambos conjuntos
interseccion = conjunto1.intersection(conjunto2)
print(interseccion)
print(" ")

# Ahora veremos la diferencia
diferencia = conjunto1.difference(conjunto2) # En este caso esta mostrando los datos diferentes del conjunto 1 en diferencia al conjunto 2
print(diferencia)
print(" ")
diferencia2 = conjunto2.difference(conjunto1) # En este caso me mostrara el dato 4 y 5
print(diferencia2)