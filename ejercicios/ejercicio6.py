'''
    Ejercicio 6.->
        Escribir un programa en el cual se ingresen cuatro numeros enteros, calcular e informar la suma de los dos primeros y el producto del tercero y el cuarto
'''

# Primero debemos solicitar los cuatro numeros al Usuario

numero1 = int(input("Favor ingresar el primer numero: "))
numero2 = int(input("Favor ingresar el segundo numero: "))
numero3 = int(input("Favor ingresar el tercero numero: "))
numero4 = int(input("Favor ingresar el cuarto numero: "))

# Ahora creamos la variable suma, la cual realizara esta operacion de los dos primeros numeros

suma = numero1 + numero2

# Ahora creamos la variable multiplicacion, la cual usuara el tercer y cuarto numero

producto = numero3 * numero4

# Ahora mostraremos en consola los resultados

print(f"El resultado de los dos primeros numeros es: {suma}\nY el de la multiplicacion es: {producto}")