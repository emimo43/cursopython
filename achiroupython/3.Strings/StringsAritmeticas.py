# String Aritmeticas
cadena1 = "Hola Enrique "
cadena2 = "Lueiza"
numero = 1

print(cadena1 + cadena2) # Aqui estamos concatenando dos strings
print("Hola usuario: " + cadena2) # Aqui concatenamos un mensaje mas la variable
print("Hola usuario: " ,cadena2) # Aqui concatenamos con la "," la cual es otra forma de concatenacion, esta forma nos da un espacio mas al imprimir en consola
print(f"Hola usuario: {cadena2}") # Esta es otra forma de concatenar
print(type(f"Hola usuario: {cadena2}")) # Me muestra que es un string
print(f"{numero} Hola usuario: {cadena2}") # Se puede concatenar con numeros
print(type(f"{numero} Hola usuario: {cadena2}"))
print(numero, "Hola usuario: " , cadena2) # Estamos concatenando numeros y strings
print(cadena2 * 5) # Con este metodo el string cadena2 se repetira 5 veces

print(type(numero)) # Me indica que esta variable es de tipo numerico

# Ahora vamos a convertir la variable numero a Strings
print(type(str(numero))) # Con el metodo str convertimos la variable numero tipo entero a Strings
