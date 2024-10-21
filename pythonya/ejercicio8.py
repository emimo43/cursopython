'''
    Ejercicio 8 --> Calcular el sueldo mensual de un operario, conociendo la cantidad de horas trabajadas y el valor por hora
'''

# Solicitamos los datos al Usuario
horasTrabajadas = float(input("Favor ingrese la cantidad de horas trabajadas en el mes: "))
valorHora = float(input("Favor ingresar el valor de la hora trabajada por el Empleado: "))

# Ahora creamos una variable llamada sueldo total en la cual almacenaremos el sueldo del Empleado

sueldoTotal = horasTrabajadas * valorHora
sueldoTotal = round(sueldoTotal,2) # Con la funcion round() dejaremos en dos los decimales

# Ahora mostramos por pantalla el resultado y ademas con la funcion type veremos de que tipo de dato es esta variable

print(type(sueldoTotal))
print(f"El sueldo total del mes del Empleado es: {sueldoTotal}")
print("\nFin del Programa")