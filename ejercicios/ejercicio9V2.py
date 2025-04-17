'''
    Ejercicio 9 -> Problema -> Ingresar el sueldo de una Persona, si supera los 3000 dolares, mostrar un mensaje en pantalla indicando que debe abonar impuestos
'''
# Solicitamos los datos al Usuario
sueldo = int(input("Favor ingresar el sueldo del Trabajador: "))

# Ahora generamos la condicion IF para ver si esto es verdadero o no
if sueldo > 3000:
    print(f"El sueldo del trabajador es {sueldo}, debe abonar impuestos")
    
print("Fin del programa")    