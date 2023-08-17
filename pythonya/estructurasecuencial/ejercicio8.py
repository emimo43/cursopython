"""Calcular el sueldo mensual de un operario, conociendo la cantidad de horas trabajadas y el valor por hora"""

#Solicitamos los datos al usuario
print("Favor ingresar las horas trabajadas por el operario: ")
horasTrabajadas = int(input()) # Casteamos el str por entero
print("Favor ingresar el valor por hora del operario: ")
valorHora = int(input())

# Ahora calculamos con la variable sueldo el total del sueldo mensual
sueldo = horasTrabajadas * valorHora

# Ahora mostramos por consola el resultado
print(f"El sueldo mensual del operario es: {sueldo}")