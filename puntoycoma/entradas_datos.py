# Clase de la funcion input -> ingreso de datos por teclado
nombre = input("Ingresa tu nombre: ")
print(f"Hola, {nombre}")
print(f"El tipo de dato de la variable nombre es: ", type(nombre))

edad = input("Ingrese su edad: ")
print(edad)
print(type(edad))

edad2 = input("Ingrese su edad: ")

if int(edad2) > 18:
    print("Puede manejar")
else:
    print("No puede manejar")    