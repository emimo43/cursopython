print("Bienvenido a mi primer programa")
print("Tipo entero")
print(type(23))
print("Tipo decimal")
print(type(12.32))
print("Tipo Cadena")
print(type("Saludos"))
print("Tipo Booleando")
print(type(False))

# Ejemplos con cadenas
print("Hola, "+" amigos!!!") # Aqui estamos concetanando dos string
print("Saludo " * 4) # Con esta formula, estamos repitiendo cuatro veces la cadena

#variable = "cadena en variable" # Estamos asignando un valor a la variable
variable = "Sumo esto a cadena en variable" #+ variable #Estamos concatenando
print(variable) # Se juntan las dos variables

print(variable[3]) # Aqui obtenemos la letra o, el espacio tambien se cuenta como caracter

print(variable[-1]) # Comienza contando al revez, en este caso con la letra e

# Ver trozos de cadena
print(variable[2:5]) # Nos muestra las letras m y o, la o es la letra antes del 5

# Imprimir longitud, con la funcion len()
print(len(variable)) # El largo de la cadena es de 30 caracteres

# Ahora veremos el metodo upper() el cual pone los caracteres en mayusculas y lower() en minusculas
print("Hola".upper())
print(variable.lower())

# Ahora veremos el metodo capitalize() el cual pone el primer caracter en mayuscula
print(variable.capitalize())

# Quitar los espacios en blanco con el metodo strip() solo los del principio y el final es lo que quita
cadena = "    Esto es una cadena con       muchos espacios    "
print(cadena)
print(cadena.strip())

# Reemplazar valores de una cadena con el metodo
cadena = "Hola esto es un texto sin reemplazar"
print(cadena)
print(cadena.replace("sin reemplazar","reemplazado"))