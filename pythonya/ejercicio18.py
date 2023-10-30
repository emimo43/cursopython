"""Un postulante a un empleo, realiza un test de capacitacion, se obtuvo la siguiente informacion, cantidad total de preguntas que se realizaron y la cantidad de preguntas que contesto correctamente. Se pide confeccionar un programa que ingrese los datos por teclado e informe el nivel del mismo segun el porcentaje de respuestas correctas que ha obtenido y sabiendo que

Nivel maximo: Porcentaje >= 90%
Nivel Medio: Porcentaje >= 75% y < 90%
Nivel Regular: Porcentaje >= 50% y < 75%
Fuera de Nivel: Porcentaje <= 50%

La formula del porcentaje es: 
porcentaje = totalcorrectas * 100 / totalpreguntas



"""
# Solicitamos los datos al Usuario
preguntasRealizadas = int(input("Favor ingresar la cantidad de preguntas realizadas: "))
preguntasCorrectas = int(input("Favor ingresar el total de preguntas correctas: "))

# Ahora creamos la formula para el porcentaje
porcentaje = (preguntasCorrectas * 100) / preguntasRealizadas

# Ahora entramos al tema del ciclo if
if(porcentaje >= 90):
    print("Nivel Maximo")
else:
    if(porcentaje >= 75 and porcentaje < 90):
        print("Nivel Medio")
    else:
        if(porcentaje >= 50 and porcentaje < 75):
            print("Nivel regular")
        elif(porcentaje <= 50):
            print("Fuera de Nivel")
