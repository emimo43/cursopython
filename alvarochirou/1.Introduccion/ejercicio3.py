"""Ejercicio 3: Problema:
Realizar la carga de dos numeros enteros por teclado e imprimir su suma y producto."""

# Solicitamos los datos al Usuario.
numero1 = int(input("Favor ingresar el primer numero entero: "))
numero2 = int(input("Favor ingresar el segundo numero entero: "))

# Ahora creamos la variable suma y producto y luego mostramos el resultado de ambas operaciones
suma = numero1 + numero2
producto = numero1 * numero2

print(f"El valor de la suma de los dos numeros es: {suma}")
print(f"El valor de la multiplicacion de ambos numeros es: {producto}")