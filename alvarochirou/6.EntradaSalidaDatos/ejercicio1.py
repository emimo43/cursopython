"""Ejercicio 1

Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”

"""
#3x^2-5x+2=0    x=1 x=2/3
from math import sqrt
# Solicitamos los valores de las variables para la ecuacion
A = int(input("Ingresa el valor de A: "))
B = int(input("Ingresa el valor de B: "))
C = int(input("Ingresa el valor de C: "))
x1 = 0
x2 = 0

# El valor de la raiz cuadrada siempre debe ser positivo, por lo cual debemos validar que sea mayor que 0


# Ahora creamos la formula para realizar la ecuacion
if ((B**2)-(4*A*C)) < 0:
    print("No se puede realizar porque no se puede sacar raiz a un numero negativo")
else:
    x1 = (-B + sqrt((B**2)-(4*A*C)))/(2*A)
    x2 = (-B - sqrt((B**2)-(4*A*C)))/(2*A)
    print("La solucion es: \nx1=",x1, "\nx2=",x2)
    print(f"La solucion es: {x1} y {x2}")

