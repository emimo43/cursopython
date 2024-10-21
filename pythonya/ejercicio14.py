'''
    Ejercicio 14 --> Problema --> Confeccionar un programa que pida por teclado tres notas de un alumno. Calcule el promedio e imprima alguno de estos mensajes:
    
    Si el promedio es >=7 mostrar "Promocionado"
    Si el promedio es >= 4 y < 7 Mostrar "Regular"
    Si el promedio es < 4 mostrar "Reprobado"
'''

# Lo primero es solicitar los datos al Usuario
nota1 = float(input("Favor ingrese la primera nota del Alumno: "))
nota2 = float(input("Favor ingrese la segunda nota del Alumno: "))
nota3 = float(input("Favor ingrese la tercera nota del Alumno: "))

# Ahora sumamos las tres notas del Alumno
suma = nota1 + nota2 + nota3
print(f"La suma de las notas del Alumno es: {suma}")

# Ahora calculamos el promedio del Alumno
promedio = suma / 3
promedio = round(promedio,2)

# Ahora mostramos por consola el resultado del promedio
print(f"\nEl promedio del Alumno es: {promedio}")

# Ahora entramos a la condicion if para ver el resultado del Alumno
if promedio >= 7:
    print('\n"Promocionado"')
else:
    if promedio >= 4 and promedio < 7:
        print('\n"Regular"')
    elif promedio <= 4:
        4
        print('\n"Reprobado"')