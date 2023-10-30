# Aqui veremos el tipo format
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

print(nombre)
print(edad)

# Ahora veremos la concatenacion
print(nombre,edad)
#print(nombre + edad) # No se puede concatenar str con enteros
print(f"{nombre}, {edad} años")
print("Hola ", nombre, "tienes ", edad)
print("Hola {} tienes {}".format(nombre,edad))