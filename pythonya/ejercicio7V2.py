'''
    Ejercicio 7.- Realizar un programa que lea cuatro valores numericos e informar su suma y promedio
'''
# Solicitamos los cuatro valores numericos al Usuario
numero1 = int(input("Favor ingrese el primer valor: "))
numero2 = int(input("Favor ingrese el segundo valor: "))
numero3 = int(input("Favor ingrese el tercer valor: "))
numero4 = int(input("Favor ingrese el cuarto numero: "))

# Calculamos la suma de los cuatro valores, y lo almacenamos en una variable llamada suma
suma = numero1 + numero2 + numero3 + numero4

# AHora calculamos el promedio y lo almacenamos en una varible con este mismo nombre
promedio = suma/4

# Ahora mostramos por consola el resultado de ambas operaciones
print(f"El valor de la suma de los cuatro numeros es: {suma}\ny el promedio es: {promedio}")