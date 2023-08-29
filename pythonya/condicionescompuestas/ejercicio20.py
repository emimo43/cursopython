"""Problema: Se carga una fecha(dia,mesy año) por teclado. Mostrar un mensaje si corresponde al primer trimestre del año(Enero, Febrero o Marzo)
Cargar por teclado el valor numerico del dia, mes y año.
Ejemplo: dia: 10 - mes:2 - año: 2018"""

# Solicitamos los datos al Usuario
dia = int(input("Favor ingresar el dia: "))
mes = int(input("Favor ingresar el mes: "))
año = int(input("Favor ingresar el año: "))

# Ahora ingresaremos al ciclo para hacer las validaciones
if(mes == 1 and mes == 2 or mes == 3):
    print(f"dia: {dia} - mes: {mes} - año: {año}, esta fecha es del primer trimestre")
else:
    print("Esta fecha no corresponde al primer trimestre del año")    