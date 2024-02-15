'''
Problema:
    Confeccionar un programa que pida por teclado tres notas de un Alumno, calcule el promedio e imprima alguno de estos mensajes:
    Si el promedio es >= 7 mostrar "Promocionado"
    Si el promedio es >= 4 y < 7 mostrar "Regular"
    Si el promedio es < 4 mostrar "Reprobado"
'''
# Solicitamos los datos al Usuario
nota1 = int(input("Favor ingresar la primera nota del Alumno: "))
nota2 = int(input("Favor ingresar la segunda nota del Alumno: "))
nota3 = int(input("Favor ingresar la tercera nota del Alumno: "))

# Ahora realizamos el calculo del Promedio del Alumno
promedio = (nota1 + nota2 + nota3) / 3

# Ahora generamos la condicion if para ver los resultados
if promedio >= 7:
    print("Promocionado")
else:
    if promedio >= 4 and promedio < 7:
        print("Regular")
    elif promedio < 4:
        print("Reprobado")
        
print("")
print("Fin del programa")        