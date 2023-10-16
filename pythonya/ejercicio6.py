"""Escribir un programa en el cual se ingresen cuatro numeros, calcular e informar la suma de los dos primeros y el producto del tercero y el cuarto"""

# Solicitamos los datos al Usuario
num1 = int(input("Favor ingrese el primer numero: "))
num2 = int(input("Favor ingrese el segundo numero:"))
num3 = int(input("Favor ingrese el tercer numero: "))
num4 = int(input("Favor ingrese el cuarto numero: "))

# Ahora creamos la variable suma y producto para realizar las operaciones
suma = num1 + num2
producto = num3 * num4

# Ahora mostramos por consola el resultado de la operacion
print(f"La suma de los numeros es: {suma}")
print(f"El valor de la multiplicacion es: {producto}")