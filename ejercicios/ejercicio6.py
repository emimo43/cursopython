'''
    Ejercicio 6.- Escribir un programa en el cual se ingresen cuatro numeros, calcular e informar la suma de los dos primeros y el producto del tercero y el cuarto
'''

# Solicitamos los datos al Usuario

numero1 = int(input("Favor ingrese el primer numero: "))
numero2 = int(input("Favor ingrese el segundo numero: "))
numero3 = int(input("Favor ingrese el tercer numero: "))
numero4 = int(input("Favor ingrese el cuarto numero: "))

# Generamos la suma
suma = numero1 + numero2

# Generamos la multiplicacion
producto = numero3 * numero4

# Ahora mostramos por consola el resultado

print(f"El valos de la suma de los dos primeros numeros es: {suma}\nEl valos de la multiplicacion de los dos ultimos numeros es: {producto}")