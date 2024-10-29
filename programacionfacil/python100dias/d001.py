# En esta clase veremos lo que es el metodo imprimir en python --> print()

#print("Primer dia en Python")

# Ahora veremos el tema de las variables, tenemos una convencion de como usar las variables, que lo puedes acceder en la documentacion oficial

'''
frase_bienvenida = "Primer dia de Python" # Esto es un tipo de dato String --> str
print(frase_bienvenida)

# Reasignar variables
variable_1 = "Hola"

variable_2 = variable_1 # En este caso la variable_2 toma el valor de variable 1

print(variable_2)
'''

# Reasignar valores a variables

'''
a = "Este es mi valor inicial"
print(a)

a = "Mi valor ha cambiado"
print(a) # Aqui el valor de la variable cambio

# En Python no necesitas poner un ; para finalizar una instruccion
'''

# Entrada de datos al programa --> Esto se hace con la funcion input()

'''
nombre = input("Por favor, introduce tu nombre: ") # El dato quedara ingresado en la variable nombre
print(nombre) # Aqui se muestra el nombre por consola

# Saltos de Linea
nombre = input("Por favor, introduce tu nombre:\n") # El dato quedara ingresado en la variable nombre
print(nombre) # Aqui se muestra el nombre por consola
# Para saltar de linea si no tienes el espacio en las comillas se ocupa el parametro \n

'''
'''
# Concatenacion en Python -> Se usa el operador +
nombre = input("Por favor, introduce tu nombre: ")
print("Bienvenido/a " + nombre + ".")
# Mejor forma es mediante f()
print(f"Bienvenido/a {nombre}.")
'''
# Comentarios en Python

# Este es un comentario de Python