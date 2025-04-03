'''
    Ejercicio 3.->
        Realizar la carga de dos numeros enteros por teclado, e imprimir su suma y producto-
'''

# Solicitamos los datos al Usuario
numero1 = int(input("Favor ingresar el primer numero: "))
numero2 = int(input("Favor ingresar el segundo numero: "))

# Creamos las variables suma y producto que nos solicitan

suma = numero1 + numero2
producto = numero1 * numero2

# Mostramos por consola el resultado de las operaciones
print(f"El valor de la suma es: {suma}")
print(f"El valor de la multiplicacion es: {producto}")