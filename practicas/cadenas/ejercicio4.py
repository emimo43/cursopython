"""Problema:
Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar(Se ingresa un valor entero en el precio del producto)"""

def precio():
    precio = int(input("Ingrese el valor del producto a llevar: "))
    cantidad = int(input("Ingrese la cantidad del producto a llevar: "))
    precio_total = precio * cantidad
    return precio_total
precio_final = precio()

print(f"El precio final del producto es {precio_final}")