'''
    Problema -> Realizar la carga de dos numeros enteros por teclado e imprimir su suma y su producto
'''
# Solicitamos los datos al Usuario
numero1 = int(input("Favor ingresar el primer numero entero: "))
numero2 = int(input("Favor ingresar el segundo numero entero: "))

# Ahora creamos la variable suma y producto
suma = numero1 + numero2
producto = numero1 * numero2

# Ahora mostramos por consola el resultado de ambas operaciones
print(f"El resultado de la suma de ambos numeros es: {suma}")
print(f"\nEl resultado de la multiplicacion de ambos numeros es: {producto}")
print(" ")
print("Fin del programa")
