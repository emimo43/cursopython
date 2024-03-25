'''
    Ejercicio 3:
    Problema:
        Realizar la carga de dos numeros enteros por teclado e imprimir su suma y producto
'''

# En primer lugar solicitamos los datos al Usuario
numero1 = int(input("Favor ingresar el primer numero entero: "))
numero2 = int(input("Favor ingresar el segundo numero entero: "))

# Ahora creamos la variable suma y producto y realizamos el calculo solicitado
suma = numero1 + numero2
producto = numero1 * numero2

# Ahora mostramos por consola el resultado de ambas operaciones
print(f"El resultado de la suma de los numeros {numero1} + {numero2} es {suma}")
print(f"El resultado de la multiplicacion de los numeros {numero1} * {numero2} es {producto}")
print("")
print("Fin del programa")