"""Problema: Ingresar el sueldo de una Persona, si supera los 3000 dolares mostrar un mensaje en pantalla indicando que debe abonar impuestos"""

# Solicitamos los datos al usuario
sueldo = int(input("Favor ingresar el sueldo del Empleado: "))

if(sueldo > 3000):
    print(f"El sueldo del Empleado es de {sueldo} debe abonar impuestos")