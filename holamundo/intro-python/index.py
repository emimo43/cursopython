"""# Este es un nuevo archivo en Python.
if 5 > 3:
    print("5 es mayor a 3 ")

# Aqui consultamos si 5 es mayor que 3, ejecutara ese codigo

# Acá va un comentario
if 3 > 5:
    print("Esto no se va a imprimir")
    # Si la condicion se cumple imprimira esta linea de codigo, por lo cual no lo va a imprimir

if 5 > 3:  # Acá va otro comentario
    print("5 es mayor a 3")"""

# Ahora veremos las variables
x = 5
y = "chanchito feliz"

# print(x, y)  # Nos imprime tanto el numero como el string

email = "chanchito@feliz.com"

# print(email)

mivar = "chanchito"

# print(mivar)

# Ahora veremos multiples variables
a, b, c = "Lala", "Lele", " Lili"

# print(a, b, c)

# Para tener variaas variables con el mismo valor esta es la forma
valor1 = valor2 = valor3 = "Chanchito Feliz"

# print(valor1, valor2, valor3)

# Concatenacion

inicio = "hola "
final = "mundo"

# print(inicio + final) # Si usamos la coma, nos mostrara dos espacios
# print(inicio, final) # Usando la coma nos da otro espacio, eso no es concatenacion

# Veamos que resulta con el metodo de format
# print(f"{inicio}{final}") # Me gusta mas esta forma

# Ahora veremos los tipos de datos

# String

palabra = "hola mundo"  # string
oracion = 'hola mundo comilla simple'  # string

# Numeros

entero = 20  # integer
conDecimales = 20.2  # float

complejo = 1j  # numero complejos, se agrega la j

# print(palabra, oracion, entero, conDecimales, complejo)

# Listas en Python

lista = [3, 2, 3]
# Lista2 va a tener una copia de lista, esto lo realiza gracias al metodo copy()
lista2 = lista.copy()
# print(lista) # Aqui vamos a imprimir la lista
# El metodo .append nos permite ingresar un elemento en la listra
lista.append(4)
# lista.clear() # El metodo .clear nos permite borrar todos los elementos de la lista

# print(lista, lista2)

"""Contando elementos y calculando el largo de una lista"""

# Con el metodo count nos permitimos ver cuantas veces se repite un dato, el cual debemos pasarlo entre parentesis
# print(lista, lista2.count(3))

# El metodo para saber cuantos elementos tiene la lista es el metodo len()
# print(len(lista), len(lista2))

# Otra forma de ver el largo de la lista es usando variables:

largoLista = len(lista)  # LargoLista almacena el largo de la lista
largoLista2 = len(lista2)

# Ahora vamos a mostrar por consola
print(largoLista, largoLista2)
