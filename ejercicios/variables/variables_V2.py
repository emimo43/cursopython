"Ejercicio sobre variables en Python"

miVariable = "Hola Mundo desde Python"
print(miVariable)
print(miVariable,"\n") # Aqui con \n damos un salto de linea

miVariable = 2 # Aqui cambiamos el valor de la variable a 2
print(miVariable, "\n")

miVariable = 10 # Aqui cambiamos el valor de la variable a 10
print(miVariable,"\n")

# Asiganamos valores a las variables
x = 10
y = 2
z = x + y # Aqui generamos la variable z, en la cual almacenamos el valor de la suma
print(f"La suma de los valores es: {z}\n")

'''
    La funcion id() nos permite saber en que espacio en memoria (direccion de memoria) esta la variable que estamos usando
'''
print(id(x))
print(id(y))
print(id(z))

'''
    Ejercicio propuesto de variables.
    Declaracion de variables, nombre, telefono y email
'''
nombre = "Enrique Lueiza"
celular = 99999999
email = "asad@gmail.com"

# AHora mostramos por consola el resultado
print(nombre)
print(celular)
print(email)