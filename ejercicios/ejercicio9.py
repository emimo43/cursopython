'''
    Ejercicio 9.-> Problema .-> Ingresar el suelto de una persona, si supera los 3000 dolares mostrar mensaje en pantalla indicando que debe abonar impuestos
'''
# Solicitamos los datos al Usuario

sueldo = int(input("Favor ingrese su sueldo: "))

# Generamos la condicion if para ver si esta se cumple

if sueldo > 3000:
    print(f"El sueldo del trabajador es: {sueldo}, debe abonar impuestos")