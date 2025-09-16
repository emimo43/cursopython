# En esta clase veremos conceptos de variables y tipos de datos

# Crearemos variables
MiVariable = "Mi string como variable" # Usar este tipo de variable no es recomendado como buena practica
# Ahora procedemos a imprimir la variable con la funcion print
print(MiVariable)

my_string_variable = "My String variable"
print(my_string_variable) # Tipo str

my_int_variable = 5 # Python ya sabe que este tipo de dato es un entero
print(my_int_variable)
print(type(my_int_variable))

# Tipo de dato bool -> Ve si es verdadero o falso, solo temos True o False como respuesta
my_bool_variable = False
print(my_bool_variable)

print(my_string_variable, my_int_variable, my_bool_variable) # Lo que imprimira por consola es una cadena de texto

my_int_variable = str(my_string_variable)
print(my_int_variable)
print(type(my_int_variable))

# En este caso estamos cambiando el tipo de dato de int a str con la funcion str()

# Concatenacion de cadena
print(type(print)) # Esta funcion es incorrecta, print es una funcion predeterminada por lo cual type() no mostrara nada

# len() es una funcion que muestra el largo de una cadena, la cantidad de caracteres
print(len(my_string_variable)) # En este caso nos mostrara la cantidad de caracteres que contiene esta variable

print("Este es el valor de: ", " ", my_bool_variable) # Aqui estamos concatenando un texto, con una variable de texto

# Variables en una sola linea

name, surname, alias, age = "Enrique", "Lueiza", "Anakin", 49

# Podemos imprimirlo ordenado o desordenado

print(name, surname, age, alias, "Mi alias es: ", alias)

# Ahora veremos la funcion de insertan datos con print()

first_name = input("¿Cual es tu nombre ? ") # Consultamos cual es tu nombre y con la funcion input logramos ingresar datos
age = input("¿Cual es tu edad ? " )

# Con la funcion print, logramos tener los datos en la consola
print(f"Mi nombre es: {first_name}")
print(f"Mi edad es: {age}, años")

# Forzar el tipo de dato

direccion : str = "Mi direccion es: "
address = 32

print(direccion)
print(address)

Address : int = 32
print(Address)

