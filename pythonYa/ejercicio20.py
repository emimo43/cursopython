'''Problema -> Ejercicio 20: 
    Se carga una fecha (dia, mes, año) por teclado. Mostrar un mensaje si corresponde al primer trimestre del año (enero, febrero, marzo). Cargar por teclado el valor numerico del dia, mes y año.
    Ejemplo: dia: 10 - mes: 2 - año: 2018
'''

# Solicitamos los datos por teclado
dia = int(input("Favor ingresar el dia en forma numerica: "))
mes = int(input("Favor ingresar el mes en forma numerica: "))
año = int(input("Favor ingresar el año en forma numerica: "))

# Ingresamos a la condicion
if mes == 1 or mes == 2 or mes == 3:
    print("Corresponde al primer trimestre del año")
    print(f"La fecha es: dia: {dia} - mes: {mes} - año: {año}")
else:
    print("La fecha no corresponde al primer trimestre")    