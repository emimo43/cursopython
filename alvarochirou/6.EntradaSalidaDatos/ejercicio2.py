"""
Ejercicio 2

Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:

PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final
"""
# Solicitamos los datos al Usuario
P1 = float(input("Favor ingrese la nota de la primera Practica: "))
P2 = float(input("Favor ingrese la nota de la segunda Practica: "))
P3 = float(input("Favor ingrese la nota de la tercera Practica: "))
EP = float(input("Favor ingrese la nota del Examen Parcial: "))
EF = float(input("Favor ingrese la nota del Examen Final: "))

# Ahora realizaremos los calculos para obtener los promedios.

# Promedio Practica 
PP = (P1 + P2 + P3) / 3
PP = round(PP,2) # Redondeo los decimales a 2 cifras

# Ahora calculamos el Promedio Final
PF = ( PP + 2*EP + 3*EF ) / 6
PF = round(PF,2) # Redondeo los dos decimales a dos cifras

# Ahora mostramos los resultados por consola
print(f"El promedio de la practica es: {PP}")
print(f"El promedio final es de: {PF}")