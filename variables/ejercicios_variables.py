# Ejercicios Variables
# 1.- Declara y asigna valores a las siguientes variables
# name = Una cadena que contenga tu nombre
# age = Un numero entero que represente tu edad
# height = Un numero flotante qye represente tu altura
# Imprime cada variable en una linea separada

# # Declaramos y asignamos las variables
# name = "Enrique Lueiza"
# age = 49
# height = 1.78

# # Ahora mostramos por consola lo solicitado
# print(f"Mi nombre es: {name}")
# print(type(name)) # Aqui mostramos el tipo de dato que contiene la variable

# print(f"Mi edad es de: {age} años")
# print(type(age))

# print(f"Mi estatura es de: {height} metros")
# print(type(height))

# # 2 .->  Convierte la variable edad de entero a cadena y concatenala con un texto que diga cuantos años tienes

# age = str(age) # Estamos convirtiendo la variable de tipo int a str
# print(type(age))
# print(f"Mi nombre es Enrique y tengo {age} años")
# print(type((f"Mi nombre es Enrique y tengo {age} años")))

# # 3.-> Declara una variable booleanda is_student que indique si eres estudiante o no. Usa TRUE o FALSE segun corresponda e imprimela

# # Declaramos la variable
# is_student = True
# print(type(is_student))
# print(is_student)

# # 4.-> Usa la funcion len() para calcular cuantos caracteres tiene tu nombre completo, almacenandolo en una variable

# # Creamos y declaramos la varible, debe ser descriptiva
# # nombre = "Enrique Antonio Lueiza Mimó"
# # print(type(nombre))
# # print(f"Mi nombre es: {nombre}")
# # print(len(nombre))

# 5.- Declara tres variables en una sola linea que represente tu nombre, apellido y ciudad, luego imprime estos valores

# Declaramos las variables

nombre, apellido, ciudad = "Enrique", "Lueiza", "Santiago"
# Mostramos por consola en una sola linea
print(f"Mi nombre es: {nombre} {apellido}, soy de {ciudad}")

print(nombre)
print(apellido)
print(ciudad)