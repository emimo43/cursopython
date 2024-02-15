'''
Problema:
    Ingresar el sueldo de una Persona, si supera los 3000 dolares mostrar un mensaje en pantalla indicando que debe abonar impuestos
'''
# Solicitamos los datos al Usuario
sueldo = float(input("Favor ingresar el sueldo del Trabajador: "))

# Ingresamos a la condicion if, donde preguntamos la condicion
if sueldo > 3000:
    print(f"Su sueldo es mayor a $3000 es de {sueldo} debe abonar impuestos")
    
    
print("Fin del programa")    