# Declaracion de multiples variables.
"""
# Asi en general declaramos las variables:
a = 5
b = 4
c = 7

# Ahora veremos la declaracion de multiples variables
"""
a,b,c = 5,3,7 # a vale 5, b vale 3, c vale 7, se mantiene el orden
# Ahora mostramos por consola los valores
print(a) # vale 5
print(b) # vale 3
print(c) # vale 7
# Ahora mostramos por consola en forma lateral
print(a,b,c) # El resultado sera 5,3,7

# Ahora ingresamos por teclado valores solicitados al usuario
print("Deme 3 valores: ")
x,y,z =input(),input(),input() # Como ingresamos tres variables, debemos ingresar 2 input(), 1 por cada variable

# Ahora creamos una variable llamada suma, en la cual sumaremos las 3 variables pero debemos castear cada una de las variables
suma = int(x) + int(y) + int(z)

# Ahora mostramos por consola el resultado de la suma
print(f"La suma de los tres numeros es:{suma}")