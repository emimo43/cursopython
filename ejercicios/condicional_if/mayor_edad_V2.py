# Ejercicio -> Determinar si una persona es mayor de edad

# Solicitamos los datos al Usuario

edad = int(input("Favor ingrese la edad de la Persona: "))

# Ahora ingresamos al condicional if para ver si la Persona cumple la condicion de mayor de edad

if edad >= 18:
    print(f"La Persona tiene {edad}, es mayor de edad")
else:
    print(f"La Persona tiene {edad}, es menor de edad")