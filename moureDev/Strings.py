# En esta clase veremos los Strings
"""Asignacion de Strings:
Consiste en asignar una cadena de caracteres a otra.
Por lo cual es necesario utilizar el operador +=
"""
print("Asignacion:")
# Vamos a crear una variable llamada mensaje y le iremos asignando datos
mensaje = "Hola" # Este es el primer texto que le asignamos
mensaje += " " # Ahora le sumamos el espacio con comillas
mensaje += "Enrique" # Ahora le sumamos mas texto, todo esto sin borrar ningun dato, esto es la asignacion de  Strings
# Ahora mostramos por consola la impresion en pantalla
print(mensaje) # Nos muestra todo lo que almaceno la variable mensaje, debido a que le hicimos asignaciones
print("\n") # Aqui creamos un salto de linea

# Ahora veremos la Concatenacion en Python
print("Concatenacion:")
# Creamos las variables
mensaje = "Hola"
espacio = " "
nombre = "Enrique"
print(mensaje + espacio + nombre)
# Esta impresion nos mostrara todo el texto concatenado con el operador +
# No se puede concatenar Strings con numeros
print("\n") # Este es un salto de Linea

# Para concatenerar Strings con numeros debemos convertir el tipo de dato numerico a str
numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos
resultado = str(resultado) # Aqui convertimos el dato numerico a String con la funcion str()
print("El resultado de la suma es; " + resultado)
# Otra forma de conversion es
print(f"El resultado de la suma es: {resultado}")
print("\n") # Salto de linea

# La busqueda
print("Busqueda:")
mensaje = ("Hola Enrique")
buscar_subcadena = mensaje.find("Enrique")
# El metodo find() nos indica desde que posicion comienza en este caso el String "Enrique"
print(buscar_subcadena) # El resultado sera 5
print("\n")

# Extraccion
print("Extraccion:")
mensaje = "Hola Enrique"
extraer_subcadena = mensaje[1:8] # Desde la posicion 1 hasta la 7 es la extraccion
print(extraer_subcadena) # Ahora mostramos la cadena extraida
print("\n")

# Comparacion
print("Comparacion:")
mensaje_uno = "Hola"
mensaje_dos = "Hola"
print(mensaje_uno == mensaje_dos)
print("\n")
