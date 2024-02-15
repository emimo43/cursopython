'''
Realizar una compra de productos (todos salen 50$) en una tienda online, calcular el costo total de la compra. Si se compran mas de 5 productos, obtiene un descuento del 20%'''

# Declaramos las variables y solicitamos los datos al Usuario
producto = int(input("Favor ingresar la cantidad de productos a comprar: "))
#precio = 50
precio = int(input("Favor ingresar el valor del precio: "))

# Ahora realizamos la operacion de costo total
precio_total = producto * precio

# Ahora realizamos un ciclo if para ver si obtiene descuento
if producto >= 5:
    descuento = precio_total * 0.20
    precio_descuento = precio_total - descuento
    print(f"El precio aplicado con el descuento del 20% es: {precio_descuento}, el precio sin descuento seria {precio_total}")
else:
    print(f"El precio total es: {precio_total}")    
    