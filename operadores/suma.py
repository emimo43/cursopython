# Realizar la carga de dos numeros por teclado e imprimir su suma y producto

# Solicitar los datos al usuario
numero1 = int(input("Favor ingrese el primer numero: "))
numero2 = int(input("Favor ingrese el segundo numero: "))

# Ahora generamos la variable suma y producto y realizamos la operacion que nos pide
suma = numero1 + numero2
producto = numero1 * numero2

# Ahora mostramos por consola el resultado
print(f"La suma de los dos numeros es: {suma}")
print(f"La multiplicacion de ambos numeros es: {producto}")