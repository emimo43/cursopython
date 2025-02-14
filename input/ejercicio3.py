'''
    Ejercicio 3.- Realizar la carga de dos numeros enteros por teclado e imprimir su suma y su producto
'''

# Solicitamos los datos al Usuario
numero1 = int(input("Favor ingresar el primer numero entero: "))
numero2 = int(input("Favor ingresar el segundo numero entero: "))

# Ahora creamos las variables suma y producto
suma = numero1 + numero2
producto = numero1 * numero2

# Ahora mostramos por pantalla los resultados de las operaciones
print(f"La suma de los numeros es: {suma}")
print(f"La multiplicacion de los numeros es: {producto}")