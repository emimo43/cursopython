cadena = "Hola Enrique"
cadena2 = "Lueiza"
numero = 1

print(cadena +" "+ cadena2) # Esto es la concatenacion
print(f"{cadena} {cadena2}")
print(cadena2 * 5) # Me mostrara esta cadena 5 veces
print("Hola usuario: " + cadena2) # Concatenar con un mensaje con el simbolo +
print("Hola usuario: ",cadena2) # Concatenar con un mensaje con la coma ,
print(f"Hola usuario: {cadena2}") # La forma en que yo lo uso
print(f"{numero} Hola Usuario: {cadena2}") # Los numeros se puede concatenar con la coma o el f

print(type(numero)) # Me indicara que es un numero entero

# Ahora convertiremos la variable numero a str
print(type(str(numero)))