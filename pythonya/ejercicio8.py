"""Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadadas y el valor por hora"""

# Solicitamos los datos al Usuario

horasTrabajadas = float(input("Favor ingresar la cantiad de horas trabajadas por el empleado: "))
valorHora = int(input("Favor ingresar el valor por hora del empleado: "))

# Ahora creamos la variable donde guardaremos el valor total del empleado

sueldo = horasTrabajadas * valorHora
print(f"EL sueldo total del empleado es: {sueldo}")
print(type(sueldo))