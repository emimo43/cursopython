# Veremos format
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

print(nombre, edad) # Esto es la concatenacion, se usa con la coma ","
print(edad)

# Ahora veremos el format
print("Hola ", nombre, "tienes ", edad) # Esto es concatenacion todavia

print("Hola {} tienes {}".format(nombre, edad))

print(f"Hola {nombre} tienes {edad} años") # El format mas practico