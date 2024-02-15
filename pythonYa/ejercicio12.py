'''
Problema:
    Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete, mostrar un mensaje "Promocionado"
'''
# Solicitamos los datos al Usuario
nota1 = int(input("Favor ingresar la primera nota: "))
nota2 = int(input("Favor ingresar la segunda nota: "))
nota3 = int(input("Favor ingresar la tercera nota: "))

# Ahora realizamos el calculo del promedio
suma = nota1 + nota2 + nota3
promedio = suma / 3

# Ahora mostramos por consola el mensaje indicado
if promedio >= 7:
    print("Promocionado")