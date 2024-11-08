'''
    Ejercicio 8.- Calcular el sueldo mensual de un operario conociendo la cantidad de horas trabajadas y el valor por hora
'''
# Solicitamos los datos al Usuario
horas_trabajadas = float(input("Favor ingresar la cantidad de horas trabajadas: "))
valor_hora = float(input("Favor ingresar el valor por hora: "))

# Ahora realizamos el calculo del sueldo total del trabajador
sueldo = horas_trabajadas * valor_hora
sueldo = round(sueldo,2) # Con la funcion round() podemos dejar cierta cantidad de decimales

# Ahora mostramos por consola el resultado del sueldo total
print(f"El sueldo mensual del trabajador es: {sueldo}")