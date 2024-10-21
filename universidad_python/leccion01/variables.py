# En esta clase veremos las variables en Python

miVariable = "Hola Mundo desde Python"
print(miVariable)
print(miVariable,"\n")
miVariable = 2
print(miVariable,"\n")
miVariable = 10
print(miVariable,"\n")

x = 10
y = 2
z = x + y
print(f"La suma de los valores es: {z}\n")

# La funcion id() nos permite saber en que espacio en memoria (direccion de memoria) esta la variable que estamos usando

print(id(x))
print(id(y))
print(id(z))

# Ejercicio Propuesto de Variables
# Declaracion de variables, nombre, telefono y email

nombre = "Enrique Lueiza"
celular = 999999999
email = "aaaa@gmail.com"

# Ahora mostramos por consola
print(nombre)
print(celular)
print(email)