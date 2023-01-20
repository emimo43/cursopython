'''Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”
'''

# sqrt es el metodo en Python para calcular la raiz cuadrada

from math import sqrt
# Ejemplo de sqrt
print(sqrt(100)) # Raiz cuadrada de 100

A = int(input("Favor ingrese el valor de A: "))
B = int(input("Favor ingrese el valor de B: "))
C = int(input("Favor ingrese el valor de C: "))

# La raiz cuadrada no se puede tener valor negativo o da error, por eso usamos el if, la raiz cuadrada siempre es positivo
# Inicializamos las variables en CERO
x1 = 0
x2 = 0

if((B ** 2) - (4 * A * C)) < 0:
    print("No se puede realizar porque no se puede sacar raiz a un numero negativo")

else:
    x1 = (-B + sqrt((B ** 2) - (4 * A * C)))/(2 * A)
    X2 = (-B - sqrt((B ** 2) - (4 * A * C)))/(2 * A)

print(f"La solucion  es: \nx1 = {x1}  \nx2 = {X2}")