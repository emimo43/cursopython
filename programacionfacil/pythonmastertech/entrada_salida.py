# En esta clase veremos la salida y entrada de datos, con la funcion print() - input
'''
# Entrada de datos
nombre = input("Por favor, introduce tu nombre: ")

# Salida de datos
print(f"El nombre almacenado es: {nombre}")


    Si quieres que el prompt (donde escribes los datos de entrada en la consola), aparezca en la línea de abajo, y no al lado, añade un simple salto de línea, dentro del mensaje del input():

# Entrada de datos
nombre = input("Por favor introduce tu nombre:\n")

# Salida de datos
print(f"El nombre almacenado es: {nombre}")

fragmento1 = "La programación es como la vida:"
fragmento2 = "llena de errores, pero también de posibilidades."

# concatenamos los dos strings
frase_completa = fragmento1 + fragmento2

# Imprimimos los dos strings en uno solo
print(frase_completa)

# Escape de caracteres

# Obtener comillas dobles en un str
print("\"El tiempo es oro\", me dijo") # Con este escape de caracteres obtenemos las comillas dobles

# Tambien se puede realizar con comillas simples
print('\'El tiempo es oro\', me dijo')

#Incrustando valores en las cadenas

# Solicitud de nombre
nombre = input("Por favor, introduzca su nombre:\n")

# Incrustacion del valor de la variable en la cadena
print(f"Hola, {nombre}. Tenga un maravilloso dia.")


# Solicitud de nombre
nombre = input("Por favor, introduzca su nombre:\n")

# Concatenación
print("Hola, " + nombre + ". Tenga un maravilloso día.") # Aqui concatenamos con el signo +

# Metodo capitalize() -> Deja la primera letra de una frase en mayuscula y el resto en minuscula

frase = "la imaginacion es el principio de la creacion."

# Primera letra mayuscuka
frase_convertida = frase.capitalize()

print(frase_convertida)

# Aqui ingresaremos el nombre en minuscula

# Obtiene el nombre del Usuario
nombre = input("Introduzca su nombre:\n")

# Convierte la primera letra en mayuscula
nombre_convertido = nombre.capitalize()

print(f"Hola {nombre_convertido}.")
'''
'''
    El método upper()
    El método upper() convierte el contenido de una cadena de caracteres, completamente en mayúsculas:

frase = "la imaginacion es el principio de la creacion."

# Todas las letras en mayusculas
frase_convertida = frase.upper()

print(frase_convertida)
'''
'''
    El método lower()
    El método lower() convierte el contenido de una cadena de caracteres, completamente en minúsculas:

frase = "LA imAgiNAcion ES el pRincipiO de LA CREAcion"

# Todas las letras en minusculas
frase_convertida = frase.lower() # Metodo que convierte todo a minusculas

print(frase_convertida)
'''