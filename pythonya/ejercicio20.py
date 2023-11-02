"""Ejercicio 20:
Problema: Se carga una fecha(dia,mes y año) por teclado. Mostrar un mensaje si corresponde al primer trimestre del año(Enero,Febrero o Marzo) Cargar por teclado el valor numerico del dia, mes y año:
Ejemplo: dia: 10, mes 2, año 2018"""

# Solicitamos los datos al Usuario
dia = int(input("Favor ingresar el dia: "))
mes = input("Favor ingresar el mes: ")
año = int(input("Favor ingresar el año: "))

# Ahora ingresamos a la condicion IF para resolver este enunciado
if(mes == "Enero" or mes == "Febrero" or mes == "Marzo"):
    print(f"El dia {dia} del mes  de {mes} corresponde al primer trimestre del año {año}")
else:
    print(f"El dia {dia} del mes de {mes} no corresponde al primer trimestre del año {2023}")