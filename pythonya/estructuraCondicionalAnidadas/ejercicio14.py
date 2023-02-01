"""Problema: Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el promedio e imprima alguno de estos mensajes:

Si el promedio es >=7 mostrar "Promocionado".
Si el promedio es >=4 y <7 mostrar "Regular".
Si el promedio es <4 mostrar "Reprobado"
"""
# Solicitamos los datos al Usuario
nota1 = int(input("Favor ingresar la primera nota: "))
nota2 = int(input("Favor ingresar la segunda nota: "))
nota3 = int(input("Favor ingresar la tercera nota: "))

# Calculamos el promedio
promedio = (nota1 + nota2 + nota3) / 3

# Ahora haremos la condicion anidada para ver el resultado
if(promedio >= 7):
    print("Promodionado")
elif(promedio >= 4 and promedio < 7):
    print("Regular")    
elif(promedio < 4):
    print("Reprobado")
else:
    print("Favor ingresar las notas correctas")        