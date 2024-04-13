'''
    Ejercicio 6 --> Escribir un programa en el cual se ingresan cuatro numeros, calcular e informar la suma de los dos primeros y el producto del tercero y el cuarto
'''

# Primero debemos ingresar los datos del Usuario
numero1 = int(input("Favor ingresar el primer numero: "))
numero2 = int(input("Favor ingresar el segundo numero: "))
numero3 = int(input("Favor ingresar el tercer numero: "))
numero4 = int(input("Favor ingresar el cuarto numero: "))

# Ahora realizamos las operaciones de suma y producto
suma = numero1 + numero2
producto = numero3 * numero4

# Ahora mostramos por consola el resultado de la operacion
print(f"La suma del numero {numero1} y numero {numero2} es: {suma}")
print(" ")
print(f"La multiplicacion del numero {numero1} y numero {numero2} es: {producto}")
print("Fin del programa")