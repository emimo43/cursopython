"""Ejercicio 21: Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad"""

# Solicitamos los datos al Usuario
dia = int(input("Ingresar el dia: "))
mes = int(input("Ingresar el mes: "))
año = int(input("Ingresar el año: "))

# Ingresamos al ciclo if
if(dia == 25 and mes == 12):
    print(f"El dia {dia} y mes {mes} y año {año} indica que hoy es Navidad")
else:
    print(f"La fecha ingresada, dia {dia} - mes {mes} - año {año}, no es Navidad")