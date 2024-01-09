# En esta clase veremos los tipos de datos compuestos
# Lista (Las listas se pueden modificar)
lista = ["Lucas Dalto","Soy Dalto", True,1.85] # Esto es un conjunto de dato (list)
print(lista)
# Ahora solicitamos que nos de el elemento 1
print(lista[1]) # El elemento 1 esta despues del indice(posicion) 0

# Tuplas
# Las tuplas no se pueden modificar a difirencia de las listas
tupla = ("Lucas Dalto","Soy Dalto", True,1.85)
print(tupla)
print(tupla[0]) # Buscamos un elemtno de la tupla

# Modificaremos la lista
lista[3] = "Maquinola"
print(lista[3])
print(lista)

# Conjunto (set) -> No se puede modificar -> No se puede acceder por indice
# No se puede repetir valores al imprimir, no existen datos duplicados
# Son datos desordenados
conjunto = {"Lucas Dalto","Soy Dalto", True,1.85}
print(conjunto)

# Diccionario -> Tiene clave y valor
# La estructura es key: value y separados con comas
diccionario = {
    'nombre' : 'Lucas Dalto',
    'canal' : 'Soy Dalto',
    'esta emocionado' : True,
    'altura': 1.84,
    'dato duplicado' : "Soy Dalto"
}
print(diccionario['nombre']) # Mostrara el resultado del valor nombre, aqui se agrega la clave