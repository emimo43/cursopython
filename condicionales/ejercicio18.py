"""Un postulante a un empleo, realiza un test de capacitacion, se obtuvo la siguiente informacion, cantidad total de preguntas que se le realizaron y la cantidad de preguntas que contesto correctamente. Se pide confeccionar un programa que ingrese los dos datos por teclado e informe el nivel del mismo segun el porcentaje de respuestas correctas que ha obtenido y sabiendo que:
Nivel maximo: Porcentaje >= 90%
Nivel medio: Porcentaje >= 75% y < 90%
Nivel regular: Porcentaje >= 50% y < 75%
Fuera de nivel: Porcentaje < 50%

Formula: porcentaje:
porcentaje = totalcorrectas * 100 / totalpreguntas
"""
# Se le solicita los datos al usuario
cantidadpreguntas = int(input("Favor ingresar la cantidad total de preguntas: "))
cantidadpreguntascorrectas = int(input("Favor ingresar la cantidad de preguntas correctas: "))

# Ahora realizamos el calculo del porcentaje, con la variable que llevara ese nombre
porcentaje =  cantidadpreguntascorrectas * 100 / cantidadpreguntas
 # Ahora realizamos el ciclo para ver la informacion que nos entregara la consola
if(porcentaje >= 90):
    print("Nivel maximo")
else:
    if(porcentaje >= 75 and porcentaje < 90):
        print("Nivel medio")
    elif(porcentaje >= 50 and porcentaje < 75):
        print("Nivel regular")
    elif(porcentaje <= 50):
        print("Fuera de nivel")             