"""Problema:
Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar(Se ingresa un valor entero en el precio del producto)"""

# Solicitamos los datos al Usuario
precio = int(input("Favor ingresar el valor del precio del producto: "))
cantidad = int(input("Favor ingresar la cantidad de producto a llevar: "))

# Ahora generamos una variable que se llamara precio_total donde estara la operacion del precio total

precio_total = precio * cantidad

# Ahora mostramos por pantalla el resultado

print(f"El precio total de la compra es: {precio_total}")