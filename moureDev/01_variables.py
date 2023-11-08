"""En esta clase veremos las variables"""

# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable) # Aqui estamos convirtiendo un entero a string
print(my_int_to_str_variable)
print(type(my_int_to_str_variable)) # Con el metodo type verificaremos que sea string

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print
print(my_string_variable,my_int_to_str_variable,my_bool_variable)
print("Este es el valor de:",my_bool_variable)
print(f"Este es el valor de: {my_bool_variable}")

# Algunas funciones del sistema
print(len(my_string_variable)) # La funcion len() indica cuantos caracteres tiene my string

# Variables en una sola linea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Enrique", "Lueiza", "Toño", 48
print(f"Me llamo: {name},{surname},mi edad es: {age}, y mi alias es: {alias}")

# Se debe tener mucho cuidado al crear las variables en una sola linea, se debe ser muy ordenados.

# Ahora veremos como ingresar datos por teclado
# Inputs
name = input("¿Cual es tu nombre?: ")
age = input("¿Cual es tu edad?: ")
print(name)
print(age)

# Ahora cambiamos su tipo
name = 35
age = "Enrique"
print(name)
print(age)

# Forzamos el tipo?
address: str = "Mi direccion" # -> El : str es solo para indicar que tipo de dato es la variable
address = True
address = 5
address = 1.2
print(type(address)) # Mostrara el tipo de dato