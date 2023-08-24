# Formas de usar el print

print("Hola Mundo")

# Declaramos algunas variables
x = "Develoteca"
print(x)

x = "Hola"
y = "soy"
z = "Develoteca"

print(x,y,z) # Asi imprimimos las variables serparadas en coma y toman su espacio en consola
print(x + y + z) # Con el signo mas no tendran espacio en consola, no se puede hacer esto con numeros tanto enteros o flotantes, si con la coma

# Esta es la forma en que mas me gusta mostrar por consola
print(f"{x},{y},{z}")