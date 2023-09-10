# En este clase veremos los operadores de identidad (is, is not)

frutas1 = ["manzana", "pera"]
frutas2 = ["manzana", "pera"]
frutas3 = frutas1

print(frutas3 is frutas1) # Aqui consultamos si frutas3 es un objeto igual que frutas1 -> el resultado es True

# Añadiremos un elemento a frutas3 con el metodo append()
frutas3.append("naranja")
print(frutas3)
print(frutas1)

# is not
print(frutas3 is not frutas1)# Indicara False debido a que lo niega



