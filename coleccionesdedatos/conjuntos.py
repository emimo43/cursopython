# Conjuntos es una coleccion de elementos que esta desordenado, y no tiene indice para acceder a sus elementos, y se usan llaves

conjunto_colores = {"rojo", "verde", "amarillo"}
print(conjunto_colores) # No lo imprime en orden

# Tambien podemos verlo con un ciclo for
for color in conjunto_colores:
    print(color)

# Si tratamos de acceder a una posicion, nos dara error por que esta coleccion es desordenada
# 
#  Si podemos acceder a ver la longitud con el metodo len()
print(len(conjunto_colores))  

# Si podemos agregar un elemento al conjunto con el metodo add()
conjunto_colores.add("negro")
print(conjunto_colores)

# Tambien podemos borrar elementos con el metodo remove()
conjunto_colores.remove("verde")
print(conjunto_colores)