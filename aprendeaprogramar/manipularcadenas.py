# Manipulacion de cadenas

# Para extraer una cadena utilizamos la indexacion que es []
nombre = "Enrique Lueiza"
#primer_nombre = nombre[0:4] # Aqui estamos indicando que quieremos obtener dentro de este rando los datos de la cadena, el primer caracter comienza en el 0, por lo cual siquieremos 4 numeros debemos ingresar desde 0 a 4
#primer_nombre = nombre[:4] # Python asumira que comenzamos desde el indice 0
# Ahora veremos como tomar el indice completo de mi apellido
#apellido = nombre[8:14] # El indice de finalizacion es excluyente
# Si dejas sin indice de finalizacion, python entendera que termina en la ultima letra
#apellido = nombre[8:]

#print(primer_nombre)
#print(primer_nombre)
#print(apellido)

# Veremos la forma de como extraer cada dos caracteres, primero daremos el rango completo de la cadena
#nombre_dos = nombre[0:14:2]
#print(nombre_dos)

# Como revertir una cadena
#nombre_invertio = nombre[::-1]
#print(nombre_invertio)

# La funcion slice() funciona de la misma manera pero un poco diferente
website = "http://www.google.com"
slice = slice(11,-4)
print(website[slice])
sitio = website[slice]
print(sitio)