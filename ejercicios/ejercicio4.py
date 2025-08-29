'''
    Ejercicio 4.-> Realizar la carga de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar (Se ingresa un valor entero en el precio del producto)
'''

# Solicitamos los datos al Usuario
precio = int(input("Favor ingrese el valor del producto a llevar: "))
cantidad = int(input("Favor ingresar la cantidad a llevar del producto: "))

# Ahora realizaremos el calculo de la venta, el cual almacenara en la variable venta
venta = precio * cantidad

# Ahora mostramos por consola el resultado
print(f"El valor total de la vanta es de: {venta}")