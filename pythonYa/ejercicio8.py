'''
Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora
'''
# Solicitamos los datos al Usuario
horas_Trabajadas = float(input("Ingrese la cantidad de Horas trabajadas por el Empleado: "))
valor_hora = float(input("Ingrese el valor por hora trabajada del Empleado: "))

# Ahora creamos la variable sueldo_mensual en la cual guardamos el salario del Empleado
sueldo_mensual = horas_Trabajadas * valor_hora

# Ahora mostramos en consola el resultado de esta operacion
print(f"El sueldo mensual del Trabajador es: {sueldo_mensual}")