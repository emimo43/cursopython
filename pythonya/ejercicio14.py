"""Ejercicio 14: Problema:
Confeccionar un programa que pida por teclado tres notas de un Alumno,calcule el promedio e imprima alguno de estos mensajes:
Si el promedio es >= 7 Mostrar 'Promocionado'
Si el promedio es >= 4 y < 7 mostrar 'Regular'
Si el promedio es < 4 mostrar 'Reprobado'
"""
# Solicitamos los datos al Usuario
nota1 = int(input("Favor ingrese la primera nota: "))
nota2 = int(input("Favor ingrese la segunda nota: "))
nota3 = int(input("Favor ingrese la tercera nota: "))

# Creamos una variable suma en la cual veremos la suma de las notas
suma = nota1 + nota2 + nota3
print(f"La suma de las notas del Alumno es: {suma}")

# Ahora creamos la variable promedio en el cual guardaremos este dato
promedio = suma / 3
print(f"El promedio del Alumno es: {promedio}")

# Ahora generamos la condicion IF para ver el resultado de lo solicitado
if(promedio >= 7):
    print("Promocionado")
else:
    if(promedio >= 4 and promedio < 7):
        print("Regular")
    else:
        print("Reprobado")