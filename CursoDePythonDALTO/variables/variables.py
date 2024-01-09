# En esta clase veremos las variables en Python, como su nombre lo indica, el dato varia
nombre = "Enrique" # Creo la variable declarando y la defino
nombre = "Antonio" # Aqui redefini la variable
numero = 10
numero += 5 # Aqui redifini la variable y le sume 1
numero -= 5
print(nombre)
print(numero)

# Concatenacion de String, unir cadenas de textos, el espacio es otro caracter
# Definimos las variables
nombre = "Enrique"
bienvenida = "Hola " + nombre + " ¿Como estas?"
print(bienvenida)

# Format (f string) sirve para convertir numeros a textos -> Concatenar con f
bienvenida = f"Hola {nombre} ¿Como estas?"
print(bienvenida)

# Operadores de pertenencia (in/not in), nos indican si algo esta en el codigo
print("Lucas" in bienvenida) # True
print("Lucas" not in bienvenida) # False