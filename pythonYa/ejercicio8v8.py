'''
Problema:
    Calcular el sueldo mensual de un operacio conociendo la cantidad de horas trabajadas y el valor por hora
'''
# Solicitamos los datos al Usuario
hora_trabajadas = float(input("Favor ingresar la cantidad de horas trabajadas por el empleado: "))
valor_hora = float(input("Favo ingresar el valor de hora trabajada por el empleado: "))

# Ahora realizamos el calculo del sueldo total del empleado
sueldo_total = hora_trabajadas * valor_hora
sueldo_total = round(sueldo_total,2) # Redondeamos el valor a dos decimales

# Ahora mostramos por consola el resultado de la operacion
print(f"El sueldo mensual del Empleado es: {sueldo_total}")