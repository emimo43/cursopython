"""Calcular el sueldo mensual de un operacio conociendo la cantidad de horas trabajadas y el valor por hora"""

def horas_trabajadas():
    cantidad_horas = float(input("Favor ingrese la cantidad de horas trabajadas: "))
    return cantidad_horas

def valor_hora():
    valorHora = float(input("Favor ingrese el valor de la hora: "))
    return valorHora


horasTrabajadas = horas_trabajadas()
horaValor = valor_hora()

def sueldo():
    sueldo_mensual = horasTrabajadas * horaValor
    return sueldo_mensual

sueldo_Mensual = sueldo()
print(f"El sueldo mensual del Trabajador es: {sueldo_Mensual}")