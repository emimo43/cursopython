'''
    Ejercicio 2 -> Calcular el area de un circulo con un radio dato,
    la formula es area = pi * radio **2
    la funcion pow() eleva la potencia a lo que uno necesite
    
'''
# Importamos la libreria math
import math

# Solicitamos los datos al Usuario
radio = float(input("Favor ingresar el radio del circulo: "))

# Ahora creamos la formula que nos solicitan
area = math.pi * radio **2 # Indicamos que el area es igual a pi(la cual traemos de la funcion math) se ultiplica por el radio elavado a 2

# Ahora vamos a redondear la cifra
area = round(area,2)

# Ahora haremos lo mismo pero con la funcion pow() -> la cual nos permite elevar a una cifra un numero
area2 = math.pi * radio.__pow__(2)
area2 = round(area2,2)

# Ahora mostramos por consola el resultado
print(f"El area del circulo es: {area}")
print("")
print(f"El area del circulo del area es: {area2}")