# En esta clase veremos los tipos de datos en Python
# Las variables son un espacio en memoria (Momentanea)

nombre = 'Enrique'
print(type(nombre)) # La variable nombre es de tipo str (String)

nombre = 'Enrique'
print(type(nombre))
print(type)

# La funcion type() nos permite identificar de que tipo de dato es la variable que estamos trabajando

numero = 89
print(type(numero)) # Tipo de numero entero
print(numero)

# Tipo de dato flotante
flotante = 3.14
print(type(flotante))
print(type)

# Consejos y reglas -> Las variables y constantes tienen sus reglas

# Palabras reservadas, debemos importar las librerias correspondientes
import keyword # Importamos la libreria
print(keyword.kwlist) # Y traemos el metodo kwlist

# Las constantes en Python no existen, pero por convencion se usan palabras mayusculas
cantidadPersonas = 100
print(cantidadPersonas)

cantidadPersonas = 150 # Aqui estamos modificando la variable
print(cantidadPersonas)

cantidadPersonas = 170
print(cantidadPersonas)

# Constantes, estas no existen en Python, pero existe una practica entre programadores, se usa con mayuscula

PI = 3.14
print(PI)
'''
    La constante en Python, puede variar, pero entre desarrolladores no se hace por buenas practicas
'''
'''
    Comentarios y asignacion multiple de variables
'''
nombre = "Enrique Lueiza"
print(type(nombre))
print(type)

# Este es un comentario

'''
    Este es un
    comentario
    de
    multiples
    lineas
'''
nombre = 'Enrique'
print(nombre)

nombre,apellido = 'Enrique','Lueiza' # Esto es una asignacion de multiples lineas
print(nombre)
print(apellido)
# Pero esta es una practica no recomendada