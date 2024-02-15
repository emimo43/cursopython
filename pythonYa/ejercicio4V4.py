'''
Problema:
    Realizar la carga del precio del producto y la cantidad a llevar. Mostrar cuanto se debe pagar (Se ingresa un valor entero en el precio del producto)
'''
# Solicitamos los datos al Usuario
cantidad_producto = int(input("Favor ingresar la cantidad de producto a llevar: "))
precio_producto = int(input("Favor ingresar el valor del producto: "))

# Ahora creamos una variable precio_total, la cual multiplica el precio por la cantidad de producto a llevar
precio_total = cantidad_producto * precio_producto

# Ahora mostramos por consola el valor de la venta
print(f"El precio total de la venta es: {precio_total}")