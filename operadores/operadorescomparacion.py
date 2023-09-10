# En esta clase veremos los operadores de comparacion

# Operador igual (==)
numero1 = 5
numero2 = 3
print(numero1 == numero2) # Consultamos si ambos numeros son iguales, indicara False

# Esto tambien se puede realizar con cadenas
cadena1 = "hola"
cadena2 = "hola"
print(cadena1 == cadena2) # La respuesta indicara True

# Estos operadores sirven tambien para las condicionales como la siguiente
cadena1 = "hola"
if (cadena1 == "hola"):
    print("Dijo hola")

# Operador distinto de (!=)    
numero1 = 3
numero2 = 5
print(numero1 != numero2) # Consultamos si numero1 es distinto de numero2, lo cual es cierto

# Operadores mayor que y menor que
numero1 = 3
numero2 = 5
print(numero1 > numero2) # Es False

numero1 = 3
numero2 = 5
print(numero1 < numero2) # Es True

numero1 = 3
numero2 = 5
print(numero1 >= numero2) # Es False

numero1 = 3
numero2 = 5
print(numero1 <= numero2) # Es True