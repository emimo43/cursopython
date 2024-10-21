'''
    Ejercicio 12 --> Se ingresan tres notas de un Alumno, si el promedio es mayor o igual a siete mostrar un mensaje "Promocionado"
'''
# Ingresamos las notas del Alumno
nota1 = int(input("Favor ingresar la primera nota: "))
nota2 = int(input("Favor ingresar la segunda nota: "))
nota3 = int(input("Favor ingresar la tercera nota: "))

# Ahora creamos la variable suma y luego promedio para obtener el dato solicitado
suma = nota1 + nota2 + nota3
print(f"La suma de las notas del Alumno es {suma}:\n")

promedio = suma / 3

# Ahora creamos el ciclo if para ver si logra el promocionado
if promedio >= 7:
    print((f"Promocionado\nFin del programa"))