'''
    Ejercicio 6.- Escribir un programa en el cual se ingresan cuatro numeros, calcular e informar la suma de los dos primeros y el producto del tercero y cuarto
'''
# Solicitamos los numeros al Usuario
numero1 = int(input("Favor ingrese el primer numero: "))
numero2 = int(input("Favor ingrese el segundo numero: "))
numero3 = int(input("Favor ingrese el tercer numero: "))
numero4 = int(input("Favor ingrese el cuarto numero: "))

# Calculamos la suma de los dos primeros numeros, lo almacenamos en la variable suma
suma = numero1 + numero2

# Calculamos ahora la multiplicacion del tercer y cuarto numero
producto = numero3 * numero4

# Ahora mostramos por consola el resultado de estas dos operaciones
print(f"La suma de los dos primeros numeros es: {suma}")
print(f"La multiplicacion de los numeros tercero y cuarto es: {producto}")