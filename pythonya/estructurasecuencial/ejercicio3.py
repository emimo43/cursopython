"""
Problema: Realizar la carga de dos numeros enteros por teclado e imprimir su suma y producto

"""
# Solicitamos los datos al usuario
print("Favor ingrese el primer numero: ")
numero1 = int(input())
print("Favor ingrese el segundo numero: ")
numero2 = int(input()) # Aqui casteamos el string a entero

# Ahora realizamos las operaciones solicitadas, que es la suma y la multiplicacion
suma = numero1 + numero2
multiplicacion = numero1 * numero2

# Ahora mostramos por consola los resultados
print(f"La suma de los dos numeros ingresados es: {suma}")
print(f"La multplicacion de los dos numeros es: {multiplicacion}")
