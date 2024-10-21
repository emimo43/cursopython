'''
    Ejercicio --> Determinar si un numero es par o impar
'''

# Solicitamos los datos al Usuario
numero = int(input("Favor ingrese un numero: "))

# Ahora ingresamos a la condicion if
if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")