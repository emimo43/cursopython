"""Ejercicio 9:
Problema: Ingresar el sueldo de una persona, si supera los 3000 dolares mostrar un mensaje en pantalla indicando que debe abonar impuestos"""

# Solicitamos los datos al Usuario

sueldo = int(input("Favor ingrese el sueldo del Trabajador: "))

# Ahora usamos la condicion if para obtener el resultado de la operacion
if(sueldo > 3000):
    print(f"El sueldo del Trabajador es de: {sueldo} debe abonar impuestos")