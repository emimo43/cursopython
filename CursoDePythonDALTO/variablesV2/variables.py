# Definiendo una variable
nombre = "Enrique Lueiza"
print(nombre)
nombre = "Antonio"
print(nombre)

# Definiendo una variable con camelCase
nombreCompletoDeTuTioMaster = "Enrique Antonio Lueiza Mimo" # No es una opcion recomendable
print(nombreCompletoDeTuTioMaster)

# Definiendo una variable con snake_cade
nombre_completo_de_tu_tio_master = "Enrique Antonio Lueiza Mimo" # Esta opcion de variable es recomendada por python.org
print(nombre_completo_de_tu_tio_master)

numero = 10
numero += 5 # sumamos 1 al valor 10
numero -=5
print(numero)

# Concatenacion
nombre = "Lucas"
# Concatenar con +
bienvenida = "Hola " + nombre + " ¿Como estas?"
# Concatenar con f
bienvenida2 = f"Hola {nombre} ¿como estas?"
print(bienvenida)
print(bienvenida2)
#del nombre # La funcion del borra la variable, ahora lo veremos con la funcion print
#print(nombre) # La consola indica que la variable nombre no esta definida, debido a que la borramos con la funcion del

# operadores de pertenencia (in / not in)
print("ola" in bienvenida) # Nos inidca True, debido a que ese trozo de string si esta en el string bienvenida
print("Hola" not in bienvenida) # la funcion not indica no es o no esta
print("Enrique" in bienvenida) # False
print("Enrique" not in bienvenida) # True