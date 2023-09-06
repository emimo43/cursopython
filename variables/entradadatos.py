# En este clase veremos como ingresar datos
nombre = input("¿Cual es tu nombre? ")
edad = int(input("¿Cuantos años tienes? "))
altura = float(input("¿Que tan alto eres? "))
edad = edad + 1
#print("Hola "+ nombre)
# Usaremos el tipo format
print(f"Hola {nombre}, tu edad es: {edad} años")
print(f"Tienes: {edad} años")
print(f"Mides {altura} cm")

# La entrada de datos siempre son str