"""Problema: Escribir un programa en el cual se ingresan cuatro numeros, calcular e informar la suma de los dos primeros y el producto del tercero y el cuarto."""

# Solicitamos los datos al usuario
num1 = int(input("Favor ingresar el primer numero: "))
num2 = int(input("Favor ingresar el segundo numero: "))
num3 = int(input("Favor ingresar el tercer numero: "))
num4 = int(input("Favor ingresar el cuarto numero: "))

# Ahora realizamos las operaciones que nos solicitan, con los dos primeros hacemos una suma, y con el tercero y cuarto la multipñlicacion

suma = num1 + num2
producto = num3 * num4

# Ahora mostramos por consola
print(f"El valor de la suma es: {suma}")
print(f"El valor de la multiplicacion es: {producto}")
