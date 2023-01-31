"""Problema: Calcular el sueldo mensual de un operacio conociendo la cantidad de horas trabajadas y el valor por hora"""

# Solicitamos los datos al usuario de la cantidad de horas trabajadas
horasTrabajadas = int(input("Favor ingresar la cantidad de horas trabajadas por el operario: "))
valorHora = int(input("Favor ingresar el valor por hora trabajada: "))

# Ahora realizamos la operacion para calcular el sueldo mensual
sueldoMensual = horasTrabajadas * valorHora

# Ahora mostramos por consola el resultado de la operacion
print(f"El sueldo menssual del trabajador es: {sueldoMensual}")