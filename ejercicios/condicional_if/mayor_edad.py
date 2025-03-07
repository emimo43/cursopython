# Determinar si una persona es mayor de edad

# Primero solicitamos los datos al Usuario

edad = int(input("Favor ingrese la edad de la Persona: "))

# Ingresamos la condicion If para ver si la Persona es mayor de edad o no
if edad >= 18:
    print(f"La edad de la Persona es: {edad} años, eres mayor de edad")
else:
    print(f"La edad de la Persona es: {edad} años, no eres mayor de edad")