'''
    Determinar si es mayor de edad
'''
# Solicitamos los datos al Usuario
edad = int(input("Favor ingrese la edad de la Persona: "))

# Ingresamos a la condicion if para ver si la Persona es Mayor de edad
if edad >= 18:
    print(f"La edad de la Persona es: {edad} años, eres mayor de edad")
else:
    print(f"Le edad de la Persona es: {edad} años, eres menor de edad")