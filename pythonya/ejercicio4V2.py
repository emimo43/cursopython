'''
    Problema -> Realizar la carga del precio del producto y la cantidad a llevar. Mostrar cuanto se debe pagar (se ingresa un valor entero en el precio del producto)
'''

# Creamos una funcion llamada venta_total
def venta_total():
    # Solicitamos los datos al Usuario
    precio = int(input("Favor ingresar el precio unitario del producto: "))
    cantidad = int(input("Favor ingresar la cantidad de producto a llevar: "))
    # Ahora generamos la variable precio_total, la cual nos dara el valor total de la venta
    precio_total = precio * cantidad
    return(f"El valor total de la venta es: {precio_total}")

venta_final = venta_total()
print(venta_final)