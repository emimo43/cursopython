'''Escribir un programa en el cual se ingresen cuatro numeros, calcular e informar la suma de los dos primeros y el producto del tercero y cuarto'''

# Declaramos las variables y solicitamos los datos al Usuario
numero = int(input("Favor ingresar el primer numero: "))
numero2 = int(input("Favor ingresar el segundo numero: "))
numero3 = int(input("Favor ingresar el tercer numero: "))
numero4 = int(input("Favor ingresar el cuarto numero: "))

# Ahora realizamos las operaciones solicitadas
suma = numero + numero2
producto = numero3 * numero4

# Ahora mostramos por consola los resultados de las operaciones
print(f"La suma de los dos primeros numeros es: {suma}")
print(f"La multiplicacion de los dos ultimos numeros es: {producto}")