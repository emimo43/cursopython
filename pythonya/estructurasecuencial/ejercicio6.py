# Escribir un programa en el cual se ingresen cuatro numeros, calcular e informar la suma de los dos primeros y el producto del tercero y cuarto

# Solicitamos los datos al usuario
print("Ingrese el primer numero: ")
numero1 = int(input())
print("Ingrese el segundo numero: ")
numero2 = int(input())
print("Ingrese el tercer numero: ")
numero3 = int(input())
print("Ingrese el cuarto numero: ")
numero4 = int(input())

# Ahora realizamos las operaciones solicitados
# Suma de los dos primeros
suma = numero1 + numero2
# Multiplicacion
producto = numero3 * numero4

# Ahora mostramos por consola el resultado de lo solicitado
print(f"La suma de los dos primeros numeros es: {suma}")
print(f"La multiplicacion de los dos numeros es: {producto}")