'''
Problema:
    Un postulante a un empleo, realiza un test de capacitacion, se obtuvo la siguiente informacion, cantidad total de preguntas que se realizaron y la cantidad de preguntas que contesto correctamente. Se pide confeccionar un programa que ingrese los dos datos por teclado e informe el nivel del mismo segun el porcentaje de respuestas correctas que ha obtenido y sabiendo que:
    
    Nivel Maximo: Porcentaje >= 90%
    Nivel Medio: Porcentaje >= 75% y < 90%
    Nivel Regular: Porcentaje >= 50% y < 75%
    Fuera de Nivel: Porcentaje < 50%
'''
# Solicitamos los datos al Usuario
preguntas_realizadas = int(input("Favor ingrese la cantidad de preguntas realizadas al postulante: "))
preguntas_correctas = int(input("Favor ingrese la cantidad de preguntas correctamentes respondidas por el postulante: "))

# Realizamos el calculo de la formula para el calculo del porcentaje, la almacenamos en la variable porcentaje
porcentaje = (preguntas_correctas * 100) / preguntas_realizadas

# Ahora ingresamos a la sentencia condicional if a realizar el procedimiento
if porcentaje >= 90:
    print("Nivel maximo")
elif porcentaje >= 75 and porcentaje < 90:
    print("Nivel medio")
elif porcentaje >= 50 and porcentaje < 75:
    print("Nivel regular")
else:
    print("Fuera de nivel")        