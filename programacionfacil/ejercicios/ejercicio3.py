'''
    Problema -> Ejercicio3 --> Realizar la carga de dos numeros enteros por teclado e imprimir su suma y producto
'''

# Solicitamos los datos al usuario
numero1 = int(input("Favor ingresar el primer numero entero: "))
numero2 = int(input("Favor ingresar el segundo numero entero: "))

# Creamos dos variables que realizaran tanto la suma como la multiplicacion
suma = numero1 + numero2
producto = numero1 * numero2

# Ahora mostramos por consola el resultado de ambas operaciones
print(f"La suma del numero  {numero1} y numero  {numero2} es: {suma}")
print(" ")
print(f"La multiplicacion del numero  {numero1} y numero  {numero2} es: {producto}")
print(" ")
print("Fin del programa")