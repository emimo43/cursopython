'''
    Problema -> Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuando se debe pagar (Se ingresa un valor entero en el precio del producto)
'''

# Solicitamos los datos al Usuario
precio = int(input("Favor ingrese el valor del producto a llevar: "))
cantidad = int(input("Favor ingresar la cantidad a llevar del producto: "))

# Ahora realizamos el calculo de la venta, el cual almacenaremos en la variable venta
venta = precio * cantidad

# Ahora mostramos por consola
print(f"El valor total de la venta es: {venta}")
