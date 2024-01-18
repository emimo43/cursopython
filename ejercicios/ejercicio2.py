'''Construye un programa que, al recibir como datos el costo de un articulo vendido, y la cantidad de dinero entregada por el cliente, calcule e imprima:
1.- El cambio que se debe entregar al cliente, si el pago efectuado es mayor que el precio del producto.
2.- ¿Que pasa si el cliente paga exactamente lo que vale el producto?
3.- La cantidad de dinero que falta por pagar, si el pago efectuado es menor que el precio del producto'''

# Declaramos las variables solicitandole los datos al usuario
costo_venta = float(input("Favor ingrese el precio del articulo en venta: "))
dinero_entregado = float(input("Favor ingresar la cantidad del dinero entregado: "))

if dinero_entregado > costo_venta:
    cambio = dinero_entregado - costo_venta
    print(f"El vuelto que se le debe al cliente es de: {cambio}")
    
if dinero_entregado == costo_venta:
    print("El dinero entregado esta exacto al precio de venta")
    
if costo_venta > dinero_entregado:
   deuda = costo_venta - dinero_entregado
   print(f"Al cliente le falta por pagar la cantidad de: {deuda} ")        