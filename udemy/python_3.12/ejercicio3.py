# Clase de variables, constantes
import constante

variable = "Enrique" # Tipo de dato string
print(variable)
print(f"Mi nombre es {variable}", type(variable))

variable = 15 # Dato int
print(variable, type(variable))

variable = False # Tipo de dato Booleando
print(variable, type(variable))

# Ahora llamamos a la constante llamada PI desde el archivo constante
print(constante.PI) # Lo importamos desde el modulo constante
print(constante,type(constante)) # Indica tipo modulo
print(constante.PI, type(constante.PI)) # Aqui indica FLOAT

# Otro tipo de orden de variables
# Variables con el mismo valor
variable1 = variable2 = variable3 = "Enrique"
print(variable1)
print(variable2)
print(variable3)

# Variable con distinto valor en una sola linea
variable1, variable2, variable3 = "Enrique", "Olivia", "Maria"
print(variable1)
print(variable2)
print(variable3)