# Programa en el que se busca el promedio de un Alumno
"""Para aprobar la nota debe ser mayor que 5"""
print("Sistema para calcular el promedio de un alumno")
nombre = input("Para comenzar, ¿Cual es tu nombre: ? ")
print(f"Mi nombre es {nombre}")

# Ahora solicitamos las calificaciones del Alumno, la cual almacenamos en variables de tipo float
quimica = float(input(f"{nombre}: ¿Cual es tu calificacion en quimica? "))
matematicas = float(input(f"{nombre}: ¿Cual es tu califacacion en matematicas? "))
biologia = float(input(f"{nombre}: ¿Cual es tu calificacion en biologia? "))

# Creamos una variable llamada promedio, donde se almacenara este valor
promedio = (quimica + matematicas + biologia) / 3
# Ahora con la funcion round() dejaremos solo con dos decimales el promedio o con uno
promedio = round(promedio,1)

# Ahora comenzamos el ciclo if
if promedio >= 6:
    print(f"Felicidades, {nombre}, El promedio es: {promedio}, 'aprobaste'")
else:
    print(f"{nombre},El promedio es: {promedio}, reprobaste")
print("Fin")
              
