# Ejercicio .- Determinar si el numero es par o impar

# Solicitamos los datos al Usuario
numero = int(input("Favor ingresar un numero: "))

# Para determinar si un numero es par o no, el modulo % debe ser igual a 0
# Ingresamos a ver esto con el condicional if

if (numero & 2 == 0):
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")