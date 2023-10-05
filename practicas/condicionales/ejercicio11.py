"""Realizar un programa que solicite la carga por teclado de dos numeros, si el primero es mayor al segundo informar su suma y diferencia, en caso contrario informar el producto y la division del primero respecto al segundo"""

# Solicitamos los datos al Usuario
numero1 = int(input("Favor ingresar el primero numero: "))
numero2 = int(input("Favor ingresar el segundo numero: "))

# Ahora vamos a realizar la condicion para solucionar el algoritmo
if(numero1 > numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    print(f"La suma de los numeros {numero1} y {numero2} es: {suma}")
    print(f"La resta de los numeros {numero1} y {numero2} es: {resta}")
else:
    producto = numero1 * numero2
    division_entera = numero1 // numero2
    division = numero1 / numero2
    print(f"La multiplicacion de los numeros {numero1} y {numero2} es: {producto}")
    print(f"La division entera de los numeros {numero1} y {numero2} es: {division_entera}")
    print(f"La division de los numeros {numero1} y {numero2} es: {division}")
