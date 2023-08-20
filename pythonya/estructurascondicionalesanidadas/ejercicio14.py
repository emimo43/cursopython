"""Problema: Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el promedio e imprima alguno de estos mensajes:
Si el promedio es >=7 mostrar "Promocionado"
Si el promedio es >= 4 y < 7 mostrar "Regular"
Si el promedio es <=4 mostrar "Reprobado"
"""

# Solicitamos los datos al usuario
nota1 = int(input("Favor ingrese la primera nota: "))
nota2 = int(input("Favor ingrese la segunda nota: "))
nota3 = int(input("Favor ingrese la tercera nota: "))

# Ahora calculamos el promedio y la almacenamos en la variable del mismo nombre
promedio = (nota1 + nota2 + nota3)/3

# Ahora realizamos el ciclo if para calcular lo que nos indican
if(promedio >= 7):
    print("Promocionado")
else:
    if(promedio >=4 and promedio < 7):
        print("Regular")
    elif(promedio < 4):
        print("Reprobado")    




           