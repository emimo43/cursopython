"""Problema: Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el promedio e imprima alguno de estos mensajes: 
Si el promedio es >= 7 mostrar 'Promocionado'
Si el promedio es >= 4 y <7 mostrar 'Regular'
Si el promedio es < 4 mostrar 'Reprobado'"""

# Lo primero que hacemos es solicitar los datos al Usuario
nota1 = int(input("Favor ingrese la primera nota: "))
nota2 = int(input("Favor ingrese la segunda nota: "))
nota3 = int(input("Favor ingrese la tercera nota: "))

# Ahora vamos a sumar las notas del alumno y la mostramos por pantalla
suma = nota1 + nota2 + nota3
print(f"La suma de las notas del Alumno es: {suma}")

# Ahora calculamos el promedio del alumno
promedio = suma / 3
print(f"El promedio del Alumno es: {promedio}")

# Ahora veremos las condiciones solicitadas y mostramos por pantalla el resultado

if(promedio >= 7):
    print("Promocionado")
else:
    if(promedio >= 4 and promedio < 7):
        print("Regular")    
    else:
        print("Reprobado")    
