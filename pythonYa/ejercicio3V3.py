'''
Problema:
    Realizar la carga de dos numeros enteros por teclado e imprimir su suma y producto
'''
# Solicitamos los datos al Usuario
numero = int(input("Favor ingrese su primer numero: "))
numero2 = int(input("Favor ingrese su segundo numero: "))

# Creamos las variables suma y producto en la cual almacenaremos los resultados de amabas operaciones
suma = numero + numero2
producto = numero * numero2

# Ahora mostramos por consola ambos resultados
print(f"La suma de ambos numeros es: {suma}")
print(f"La multiplicacion de ambos numeros es: {producto}")
print("Fin del programa")