'''
    Ejercicio 6.- Escribir un programa en el cual se ingresen cuatro numeros, calcular e informar la suma de los dos primeros y el producto del tercero y cuarto
'''
# Solicitamos los datos al Usuario
numero1 = int(input("Favor ingrese el primer numero: "))
numero2 = int(input("Favor ingrese el segundo numero: "))
numero3 = int(input("Favor ingrese el tercer numero: "))
numero4 = int(input("Favor ingrese el cuarto numero: "))

# Ahora creamos las variables suma y producto para realizar las operaciones
suma = numero1 + numero2
producto = numero3 * numero4

# Ahora mostramos por consola el resultado de las operaciones
print(f"La suma de los numeros {numero1} + {numero2} es: {suma}")
print(f"La multiplicacion de los numeros {numero3} * {numero4} es {producto}")

