'''
    Ejercicio 3.- 
    Problema -> Realizar la carga de dos numeros enteros por teclado e imprimir su suma y su producto
'''

# Solicitamos los datos al Usuario
numero1 = int(input("Favor ingrese el primer numero: "))
numero2 = int(input("Favor ingrese el segundo numero: "))

# Ahora realizaremos la suma y la multiplicacion
suma = numero1 + numero2
producto = numero1 * numero2

# Ahora mostramos los resultados por consola
print(f"La suma de los numeros {numero1} y {numero2} es: {suma}")
print(f"La multiplicadion de los numeros {numero1} y {numero2} es: {producto}")