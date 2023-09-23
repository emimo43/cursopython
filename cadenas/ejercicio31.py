# Format con string por medio de indices

cantidad = 3
numeroControl = 10
precio = 59.90

precioDeVenta = "El producto vale {2} y son {0} productos el numero de control es {1}"
# En las llaves se asigna la posicion de la variable que estan en el format()

print(precioDeVenta.format(cantidad,numeroControl,precio))