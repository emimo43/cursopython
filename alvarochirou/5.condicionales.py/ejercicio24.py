"""Ejercicio 24:
Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero con el segundo y a este resultado se lo multiplica por el tercero"""

# Ingresamos los datos del Usuario
numero1 = int(input("Favor ingrese el primer numero: "))
numero2 = int(input("Favor ingrese el segundo numero: "))
numero3 = int(input("Favor ingrese el tercer numero: "))

# Ahora generamos el condicional if
if numero1 == numero2 and numero1 == numero3:
    if numero2 == numero3:
        # Creamos la variable suma
        suma = numero1 + numero2
        print(f"El resultado de la suma es: {suma}")
        # Ahora generamos la variable resultado donde a la suma le multiplicamos el numero 3
        resultado = suma * numero3
        print(f"El resultado de la multiplicacion de la suma con el numero 3 es: {resultado}")

        
