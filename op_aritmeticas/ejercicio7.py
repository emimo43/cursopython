'''
    Ejercicio 7.-
    Realizar un programa que lea cuatro valores numericos e informar su suma y promedio
'''

# Solicitamos los datos al Usuario
numero1 = int(input("Favor ingrese el primer numero: "))
numero2 = int(input("Favor ingresar el segundo numero: "))
numero3 = int(input("Favor ingresar el tercer numero: "))
numero4 = int(input("Favor ingresar el cuarto numer0: "))

# Ahora creamos las variables suma y promedio, las cuales almacenaran los resultados
suma = numero1 + numero2 + numero3 + numero4

promedio = suma / 4

# AHora mostramos por consola los resultados obtenidos
print(f"La suma de los cuatro numeros es: {suma} y el promedio es: {promedio}")