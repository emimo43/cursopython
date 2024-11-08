'''
    Ejercicio 9.- Problema --> Ingresar el sueldo de una persona, si supera los 3000 dolares mostrar un mensaje en pantalla indicando que debe abonar impuestos
'''
# Solicitamos los datos al Usuario
sueldo = int(input("Favor ingresar el sueldo de la Persona: "))

# Ahora generamos la condicion IF para ver si esta se cumple
if sueldo > 3000: # Si la condicion se cumple, se muestra el mensaje por consola
    print("Esta persona debe abonar impuestos")