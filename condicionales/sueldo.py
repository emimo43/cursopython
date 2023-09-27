"""Problema:
Ingresar el sueldo de una persona, si supera los 3000 dolares mostrar un mensaje en pantalla indicando que debe abonar impuestos"""

# Solicitamos los datos al usuario, los cuales ingresamos en una variable

sueldo = int(input("Favor ingrese el sueldo del Trabajador: "))
# Ahora usamos la condicion if
if(sueldo > 3000):
    print("Debe abonar impuestos")