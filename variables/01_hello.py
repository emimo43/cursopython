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

