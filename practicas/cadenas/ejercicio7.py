"""Realizar un programa que lea cuatro valores numericos e informar su suma y promedio"""

# Vamos a generar dos funciones una que sea suma y otra promedio
# Funcion suma_notas
def suma_notas():
    num1 = int(input("Favor ingresar la primera nota: "))
    num2 = int(input("Favor ingresar la segunda nota: "))
    num3 = int(input("Favor ingresar la tercera nota: "))
    num4 = int(input("Favor ingresar la cuarta nota: "))
    suma = num1 + num2 + num3 + num4
    
    return suma

# Ahora generamos la funcion promedio
def promedio_notas():
    promedio = valor_suma_notas/4
    return promedio
    
valor_suma_notas = suma_notas() 
valor_promedio_notas = promedio_notas()
print(f"El valor de la suma de las notas es: {valor_suma_notas}") 
print(f"El promedio de las notas del alumno es: {valor_promedio_notas}")  