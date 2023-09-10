# Clase de operadoresde pertenencia -> permiten verificar si algo esta dentro de lista de valores o de objetos dentro de lista de objetos

# Operador in

frutas1 = ["manzana", "pera", "naranja"]
frutas2 = "pera"

print(frutas2 in frutas1) # Aqui estamos consultando si frutas2 esta en la lista de frutas1, el resultado es True

# Operador not in
print(frutas2 not in frutas1) # Aqui negara la afirmacion, dira False

frutas3 = "melocoton"
print(frutas3 not in frutas1) # Indicara True debido a que este objeto no esta en frutas1