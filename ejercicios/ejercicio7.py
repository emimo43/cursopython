'''
    Ejercicio 7.->
        Realizar un programa que lea cuatro valores numericos e informar su suma y promedio
'''

# Solicitamos los daros al usuario, cuatro valores numericos de tipo entero

numero1 = int(input("Favor ingrese el primer numero: "))
numero2 = int(input("Favor ingrese el segundo numero: "))
numero3 = int(input("Favor ingrese el tercer numero: "))
numero4 = int(input("Favor ingrese el cuarto numero: "))

# Ahora creamos las variables suma y promedio y realizamos las operaciones solicitadas

suma = numero1 + numero2 + numero3 + numero4

promedio = suma / 4

# Ahora mostramos por consola el resultado solicitado

print(f"La suma de las cuatro notas es: {suma}\nY el promedio final es: {promedio}")