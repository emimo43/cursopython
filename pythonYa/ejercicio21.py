'''
    Ejercicio 21:
        Realizar un programa que pida cargar una fecha cualquiera, luego verificar si dicha fecha corresponde a Navidad
'''

# Solicitamos los datos al Usuario
dia = int(input("Favor ingresar el dia en forma numerica: "))
mes = int(input("Favor ingresar el mes en forma numerica: "))
año = int(input("Favor ingresar el año en forma numerica: "))

# Ahora ingresamos al ciclo
if dia == 25 and mes == 12:
    print(f"Hoy es navidad es: {dia} - {mes} - {año}")
else:
    print("Hoy no es navidad")    