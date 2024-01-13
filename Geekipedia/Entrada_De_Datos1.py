# En esta clase veremos la entrada de datos por teclado en Python
# Declaramos una variable
palabra = input("Introduce una palabra: ") # La funcion input nos introduce los datos por teclado
num_int = int(input("Introduce un numero entero: "))
num_float = float(input("Introduce un numero flotante: "))
num_complex = complex(input("Introduce un numero complejo: "))

print("String: ", palabra)
print("Entero: ", num_int)
print("Flotante: ", num_float)
print("Numero Complejo: ", num_complex)