'''
    Ejercicio 3.-> Problema .-> Realizar la carga de dos numeros enteros por teclado e imprimir su suma y producto
'''

# Solicitamos los datos al Usuario
num1 = int(input("Favor ingrese el primer numero entero: "))
num2 = int(input("Favor ingresar el segundo numero entero: "))

# Declaramos las variables suma y producto donde se almacenaran las operaciones
suma = num1 + num2
producto = num1 + num2

# Ahora mostramos por consola el resultado de ambas operaciones, esto puede ser una sola linea o por separadas
print(f"La suma de los numeros {num1} + {num2} es: {suma}")
print(f"La multiplicacion de los numeros {num1} * {num2} es : {producto}")

# La forma de impirmir en una sola linea es:
print(f"EL resultado de la suma y multiplicacion de ambos numeros {num1} y {num2} -> suma {suma} -> multiplicacion -> {producto}")