'''
    Ejercicio 6 -> Escribir un programa en el cual se ingresen cuatro numeros, calcular e informar la suma de los dos primeros y el producto del tercero y cuarto
'''

# Primero solicitamos los datos al Usuario
numero1 = int(input("Favor ingresar el primer numero: "))
numero2 = int(input("Favor ingresar el segundo numero: "))
numero3 = int(input("Favor ingresar el tercer numero: "))
numero4 = int(input("Favor ingresar el cuarto numero: "))

# Ahora declaramos la variable suma y producto, con las cuales realizaremos las operaciones que nos solicitan
suma = numero1 + numero2
producto = numero3 * numero4

# Ahora vamos a mostrar por consola el resultado de ambas operaciones
print(f"La suma de los numeros {numero1} + {numero2} es: {suma}")
print(f"El valor de la multiplicacion de los numeros {numero3} * {numero4} es: {producto}")