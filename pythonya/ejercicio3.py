"""Problema: Realizar la carga de dos numeros enteros por teclado e imprimir su suma y producto"""

# Solicitamos los datos al Usuario

numero1 = int(input("Favor ingresar el primer numero: "))
numero2 = int(input("Favor ingresar el segundo numero: "))

# Ahora creamos dos variables, una llamada suma y otra llamada producto en las cuales guardaremos las operaciones

suma = numero1 + numero2
producto = numero1 * numero2

# Ahora vamos a mostrar por consola los resultados
print(f"La suma de los dos numeros es: {suma}")
print(f"La multiplicacion de los dos numeros es: {producto}")