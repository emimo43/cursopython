'''
    Problema -> Realizar la carga del precio del producto y la cantidad a llevar. Mostrar cuanto se debe pagar (se ingresa un valor entero en el precio del producto)
'''

# Se solicitan los datos al Usuario
producto = int(input("Favor ingresar la cantidad de producto a llevar: "))
precio = int(input("Favor ingresar el precio del producto a llevar: "))

# Ahora generamos una variable llamada precio_total, la cual realiza el calculo para obtener el valor de la venta total
precio_total = producto * precio

# Ahora mostramos por consola el resultado de la venta
print(f"El valor total de la venta es: {precio_total}")