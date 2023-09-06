print("Me encanta la pizza")
print("Es una delicia!")

# Declaramos variables
nombre = "Enrique"
apellido = "Lueiza"
nombreCompleto = "Hola " +nombre +" " + apellido
print(f"Hola {nombre}")
print((nombreCompleto))

# Asi se ve que tipo de variable es
print(type(nombre)) # Nos indica que la variable es de tipo str

"""Ahora veremos tipos de datos enteros"""
edad = 24 # Esto es un dato de tipo entero
#edad = edad + 1 #Aqui sumamos uno
#edad += 1 # Esto es lo mismo que lo que mostramos antes
print(edad)
print(type(edad))

# No se concatena enteros con str
# Estas son dos formas de formatear, incluye str con numeros int o float
print("Tu edad es: ", edad)
print(f"Tu edad es: {edad}")

# Tambien se puede hacer con un casting
print("Tu edad es: " + str(edad))

# Numeros flotantes

altura = 180.5
print(type(altura))
print(altura)
print(f"Tu altura es: {altura}")
print("Tu altura es: ", altura)
print("Tu altura es: "+ str(altura))

# Datos Booleanos
humano = False
print(humano)
print(type(humano))
print(f"Eres un humano:{humano}")
print("Eres un humano:",humano)
print("Eres un humano:" + str(humano))

# Asignaciones multiples de variables
"""nombre = "Enrique"
edad = 48
atractivo = True"""

nombre,edad,atractivo = "Enrique", 24, True # Esto es una asignacion multiple

# Ahora mostramos por consola
print(nombre)
print(edad)
print(atractivo)

#nombre1 = 10
#nombre2 = 10
#nombre3 = 10
#nombre4 = 10

# Esta es la mejor forma en asignacion multiple
nombre1 = nombre2 = nombre3 = nombre4 = 10

print(nombre1)
print(nombre2)
print(nombre3)
print(nombre4)

# Ahora veremos el metodo de las cadenas o str
nombre = "Enrique"
print(len(nombre)) # El metodo len nos indica la longitud de nuestra variable

print(nombre.find("E")) # El metodo find nos permite buscar la posicion de un caracter en especifico

nombre2 = "enrique"
print(nombre2.capitalize()) #El metodo capitalize()me convertira la primera letra en mayuscula, solo es la primera letra del texto, si incluimos mas texto no convertira la primera letra

print(nombre2.upper()) # El metodo upper() convertira todo el texto a mayuscula

print(nombre.lower()) # El metodo lower() coonvertira todo el texto a minuscula

print(nombre.isdigit())# El metodo isdigit() nos indicara si lo que estamos validando es un digito, en este caso indicara que es False

print(nombre2.isalpha()) # Este metodo isalpha() nos indica si son caracteres alfabeticos, en este caso indicara True, solo deben ser letras, sin espacio ni caracteres especiales

print(nombre2.count("e")) # El metodo count() nos indica cuantos caracteres de un tipo tenemos en una cadena

print(nombre2.replace("e", "a"))# El metodo replace remplaza algun caracter por otro, el primero que dejamos en los parentesis es el que vamos a remplazar por el segundo

print(nombre2 * 4) # Este metodo repetira la cadena varias veces