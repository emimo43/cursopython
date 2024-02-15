'''
Tarea 1:
    Eres un profesor y deseas crear un programa en Python para evaluar las calificaciones de los estudiantes.
    El programa debe solicitar al usuario que ingrese su calificacion como un numero decimal. Luego, debe mostrar un mensaje que refleje su rendimiento de acuerdo con ciertos criterios
    
    Problema: Calificación de Estudiantes



Descripción:

Eres un profesor y deseas crear un programa en Python para evaluar las calificaciones de los estudiantes. El programa debe solicitar al usuario que ingrese su calificación como un número decimal. Luego, debe mostrar un mensaje que refleje su rendimiento de acuerdo con ciertos criterios:



    Si la calificación es igual o mayor a 90, mostrar "¡Felicidades! Has aprobado con una calificación sobresaliente."

    Si la calificación es igual o mayor a 70 pero menor que 90, mostrar "Has aprobado satisfactoriamente."

    Si la calificación es igual o mayor a 60 pero menor que 70, mostrar "Has aprobado, pero necesitas mejorar un poco."

    Si la calificación es menor que 60, mostrar "Lo siento, has suspendido. Debes esforzarte más en la próxima evaluación."

Instrucciones:



    Usa input() para obtener la calificación como entrada y conviértela en un número de punto flotante.

    Utiliza if, elif y else para verificar las condiciones y mostrar el mensaje correspondiente según la calificación ingresada.

    Ejecuta el programa, proporciona una calificación y observa el mensaje resultante.



Este programa permite a los estudiantes comprender cómo se pueden tomar decisiones basadas en condiciones en Python y cómo personalizar mensajes en función de diferentes calificaciones.


'''

# Solicitamos los datos al Usuario
calificacion = float(input("Favor ingrese la calificacion del Estudiante: "))

# Ingresamos a la sentencia condicional if
if calificacion >= 90:
        print("¡Felicidades! Has aprobado con una calificacion sobresaliente")
elif calificacion >= 70 and calificacion < 90:
        print("Has aprobado satisfactoriamente")  
elif calificacion >= 60 and calificacion < 70:
        print("Has aprobado, pero necesitas mejorar un poco")
elif calificacion < 60:
        print("Lo siento, has suspendido. Debes esforzarte mas en la proxima evaluacion")  

print("")                