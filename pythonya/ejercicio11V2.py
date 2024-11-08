'''
    Ejercicio 11.- Realizar un programa que solicite la carga por teclado de dos numeros, si el primero es mayor al segundo, informa su suma y diferencia, en caso contrario informar el producto y la division del primero respecto al segundo
'''

# Solicitamos los dos numeros al Usuario
numero1 = int(input("Favor ingrese el primer numero: "))
numero2 = int(input("Favor ingrese el segundo numero: "))

# Ahora ingresamos al condicional IF para obtener lo solicitado
if numero1 > numero2:
    suma = numero1 + numero2
    resta = numero1 - numero2
    print(f"La suma de ambos numeros es: {suma}")
    print(f"La diferencia entre ambos numeros es: {resta}")
else:
    producto = numero1 * numero2
    division = numero1 / numero2
    division_entera = numero1 // numero2
    print(f"La multiplicacion de ambos numeros es: {producto}")
    print(f"La division entre ambos numeros es: {division}")
    print(f"La division entera entre ambos numeros es: {division_entera}")