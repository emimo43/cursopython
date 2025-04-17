'''
    Ejercicio 8.->
        Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora
'''
# Debemos solicitar los datos al Usuario, son horastrabajadas y el valor por hora

horas_trabajadas = float(input("Favor ingresar la cantidad de horas trabajadas: "))
valor_hora = int(input("Favor ingrese el valor por hora: "))

# Ahora creamos la variable sueldo mensual, la cual contendra la multiplicacion entre horas trabajadas por el valor de la hora

sueldo_mensual = horas_trabajadas * valor_hora

# Mostramos por consola el resultado

print(f"El sueldo mensual del trabajador es: {sueldo_mensual}")