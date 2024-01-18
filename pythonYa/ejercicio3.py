'''Problema: Realizar la carga de dos numeros enteros por teclado e imprimir su suma y producto.'''
# Solicitamos los datos al Usuario:
numero1 = int(input("Favor ingresar el primer numero entero: "))
numero2 = int(input("Favor ingresar el segundo numero entero: "))

# Ahora realizamos el calculo de la suma y el producto
suma = numero1 + numero2
multiplicacion = numero1 * numero2

# Ahora mostramos por consola el resultado de ambas operaciones
print(f"El valor de la suma del numero {numero1} + el numero {numero2} es: {suma}")
print(f"El valor de la multiplicacion del numero {numero1} * numero {numero2} es: {multiplicacion}")
print("Fin del programa")