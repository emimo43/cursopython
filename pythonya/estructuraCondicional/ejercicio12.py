"""Problema: Se ingresan tres notas de un Alumno, si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado"""

# Ingresamos los datos del usuario:
nota1 = int(input("Favor ingresar la primera nota: "))
nota2 = int(input("Favor ingresar la segunda nota: "))
nota3 = int(input("Favor ingresar la tercera nota: "))

# Ahora calcularemos el promedio
promedio = (nota1 + nota2 + nota3) / 3

# Ahora veremos el ciclo if
if(promedio >= 7):
    print("Promocionado")