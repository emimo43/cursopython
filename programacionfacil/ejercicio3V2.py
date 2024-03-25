'''
    Problema -> Realizar la carga de dos numeros enteros por teclado e imprimir su suma y producto
'''
num1 = int(input("Favor ingresar el primer numero entero: "))
num2 = int(input("Favor ingresar el segundo numero entero: "))

# Declaramos las variables suma y producto
suma = num1 + num2
producto = num1 * num2

# Ahora mostramos por consola el resultado de ambas operaciones, esto puede ser en una sola linea o por separado
print(f"La suma de los numeros {num1} + {num2} es: {suma}")
print(f"La multiplicacion de los numeros {num1} * {num2} es: {producto}")

# La formuala de imprimir en una sola linea es:
print(f"El resultado de la suma y multiplicacion de ambos numeros {num1} y {num2} -> suma: {suma} - multiplicacion -> {producto}")
           
