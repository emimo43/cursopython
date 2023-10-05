"""Se ingresan tres notas de un alumno, si el promedio es mayor  o igual a siete mostrar un mensaje "Promocionado"
"""

# Solicitamos los datos al Usuario
nota1 = int(input("Favor ingrese la primera nota: "))
nota2 = int(input("Favor ingrese la segunda nota: "))
nota3 = int(input("Favor ingrese la tercera nota: "))

# Ahora realizamos la suma y el promedio
suma = nota1 + nota2 + nota3
promedio = suma / 3

# Ahora ingresamos al ciclo if
if(promedio >= 7):
    print("Promocionado")
