"""Realziar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad"""

# Solicitamos los datos al usuario
dia = int(input("Favor ingresar el dia: "))
mes = int(input("Favor ingresar el mes: "))
año = int(input("Favor ingresar el año: "))

# AHora realizamos la condicion que nos permitira verificar si la fecha corresponde a navidad
if(dia == 25 and mes == 12):
    print("Es Navidad")
else:
    print("No es navidad")    