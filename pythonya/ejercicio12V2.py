'''
    Ejercicio 12.- Se ingresan tres notas de un alumno, si el promedio es mayo o igual a siete mostrar un mensaje "Promocionado"
'''

# Ingresamos las notas del Alumno
nota_1 = int(input("Favor ingrese la primera nota: "))
nota_2 = int(input("Favor ingrese la segunda nota: "))
nota_3 = int(input("Favor ingrese la tercera nota: "))

# Ahora realizamos el calculo para obtener el promedio
promedio = (nota_1 + nota_2 + nota_3) / 3

# Ahora ingresamos al condicional if para ver si se cumple la condicion requerida
if promedio >= 7:
    print("Promocionado")
