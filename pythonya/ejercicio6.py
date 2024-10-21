'''
    Ejercicio 6 --> Escribir un programa en el cual se ingresen cuatro numeros, calcular e informar la suma de los dos primeros y el producto del tercero y el cuarto
'''
# Lo primero es solicitar los datos al Usuario, en este caso seran numeros enteros
numero1 = int(input("Favor ingresar el primer numero entero: "))
numero2 = int(input("Favor ingresar el segundo numero entero: "))
numero3 = int(input("Favor ingresar el tercer numero entero: "))
numero4 = int(input("Favor ingresar el cuarto numero entero: "))

# Ahora creamos la variable suma y producto, la cual almacenaran los resultados de las operaciones solicitadas

suma = numero1 + numero2
producto = numero3 * numero4

# Ahora mostramos por consola el resultado
print(f"La suma de los dos primeros numeros es: {suma}")
print(f"\nLa multiplicacion de los dos ultimos numeros es: {producto}")
print("\nFin del programa")