'''
    Ejercicio 9.->
    Ingresar el sueldo de una persona, si supera los 3000 dolares, mostrar un mensaje en pantalla indicando que debe abonar impuestos
    
'''
# Lo primero despues del analisis, es solicitar los datos al Usuario

sueldo = int(input("Favor ingresar el sueldo del trabajador: "))

# Ahora generamos la estructura de control if para hacer que con la condicion veamos el proceso

if sueldo > 3000:
    print("El trabajador debe par impuestos")
    
print("Fin del programa")    