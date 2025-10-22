# En esta clase veremos las variables y sus tipos de uso

edad = 28 # Esta es una variable de tipo entero
print(type(edad))
print(edad)

numero_1 = 10 # Variable de tipo int
print(type(numero_1))
print(numero_1)

# Reasignaremos el valor a la variable numero_1 ahora sera de tipo str
numero_1 = "Hola" # Esta ahora es una variable de tipo str
print(type(numero_1))
print(numero_1)

# Reasignacion de variables en Python
edad = 20
print(edad)
edad = 32
print(edad)
edad = 26
print(edad)

numero_1 = 10
# Siempre se debe crear la variable e inicializarla con un valor

numero_1 = None
print(type(numero_1))
print(numero_1)

# Con el parametro None, la variable queda nula o vacia

numero_1 = int()
print(type(numero_1))
print(numero_1)

# Al inicializar la variable tipo int() pero sin un valor alguno, le indicamos que se inicaliza como entero, pero si mostramos por consola, dira valor 0

# Asignacion multiple en Python

numero_1, numero_2, numero_3 = 10, 12, 17
print(numero_1,numero_2,numero_3)
print(numero_1)
print(numero_2)
print(numero_3)

# Reasignar valores a las variables

numero_1 = 10
numero_2 = 20
print(numero_1)
print(numero_2)