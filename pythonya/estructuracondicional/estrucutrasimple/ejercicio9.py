"""Problema: Ingresar el sueldo de una persona, si supera los 3000 dolares mostrar un mensaje en pantalla indicando que debe abonar impuestos"""

# Solicitamos los datos al usuario
print("Favor ingresar el sueldo del Empleado: ")
sueldo = input()
# Ahora casteamos la variable sueldo que viene como str a entero
sueldo = int(sueldo)
# Ahora generamos la condicion if que nos pide que si el sueldo es mayo a 3000 dolares mostrar el mensaje
if(sueldo > 3000):
    print(f"El sueldo del empleado es: {sueldo}, debe abonar impuestos")