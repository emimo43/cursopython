'''
    Ejercicio 8 -> Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora
'''

# Solicitamos los datos al Usuario

horasTrabajadas = float(input("Favor ingrese la cantidad de horas trabajadas: "))
valorHora = float(input("Favor indicar el valor hora del trabajador: "))

# Ahora realizamos el calculo del valor hora del Empleado, lo almacenemos en la variable sueldo
sueldo = horasTrabajadas * valorHora

# Ahora mostramos el sueldo en consola
print(f"El sueldo total del trabajador es: {sueldo}")

# Usaremos la funcion round para dejar solo dos decimales
sueldo = round(sueldo,2)
print(f"El sueldo mensual del trabajador es: {sueldo}")
