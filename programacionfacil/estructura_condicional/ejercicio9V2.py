'''
Ejercicio 9 -> Problema -> Ingresar el sueldo de una Persona, si supera los 3000 dolares mostrar un mensaje en pantalla indicando que debe abonar impuestos
'''

# Solicitamos los datos al Usuario
sueldo = float(input("Favor ingresar el sueldo del Empleado: "))

# Ahora veremos la condicion if
if sueldo > 3000:
    print("Esta persona debe abonar impuestos")