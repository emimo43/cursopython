"""Ejercicio 12:
Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado"""

# Solicitamos los datos al Usuario
nota1 = int(input("Favor ingrese la primera nota: "))
nota2 = int(input("Favor ingrese la segunda nota: "))
nota3 = int(input("Favor ingrese la tercera nota: "))

# Ahora creamos la variable suma con la cual sumamos las 3 notas
suma = nota1 + nota2 + nota3

# Ahora mostramos por consola el resultado de esta suma
print(f"La suma de las tres notas es: {suma}")

# Ahora creamos la variable promedio en la cual guardaremos este dato
promedio = suma / 3
# Ahora mostramos por consola el promedio del alumno y luego usamos el condicional IF para ver el resultado
print(f"El promedio del Alumno es: {promedio}")

if(promedio >= 7):
    print("Promocionado")