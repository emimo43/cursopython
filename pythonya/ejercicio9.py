'''
    Ejercicio 9 --> Problema --> Ingresar el sueldo de una Persona, si supera los 3000 dolares, mostrar un mensaje en pantalla indicando que debe abonar impuestos
'''

# Lo primero que debemos hacer es solicitar los datos al Usuario

sueldo = float(input("Favor ingresar el sueldo del Empleado: "))

# Ahora usamos la condicion if para ver si el empleado cumple la condicion

if sueldo > 3000:
    print("Debe abonar impuestos")