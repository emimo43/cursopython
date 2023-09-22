"""Problema:
Hallar la superficie de un cuadrado conociendo el valor de un lado"""

# Solicitamos los datos al usuario
print("Favor ingrese el valor del lado del cuadrado")
lado = input()
lado = int(lado) # Aqui estamos casteando la variable de str a int

# Generamos una variable llamada superficie que hara el calculo
superficie = lado * lado

# Ahora mostramos por consola el valor del resultado
print(f"El valor de la superficie del cuadrado es {superficie}")
