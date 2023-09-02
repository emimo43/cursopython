# En esta clase veremos como convertir tipos de datos

x = 1
y = 2.0
z = "3"

print(x)
print(y)
print(z)

print(type(x))
print(type(int(y)))
print(type(z))

print(y)
print(x)
print(str(y))
print(float(z))

# Para que queden almacenados los cambios en las variables debemos hacer lo siguiente

y = str(y)
x = str(x)

# No se pueden sumar los str

x = 3
x = int(x)

print(type(y))
print(type(x))
y = float(y)
y = int(y)
print(type(y))

print(type(x * y))

# Para concatenar un texto con variables se debe convertir en este caso un entero
edad = 24 # Tipo de dato entero
print("Edad: " + str(edad))
print(f"Edad: {edad}") # Con el format funciona de edad manera
# Ahora veremos que tipo de dato nos muestra la variable
print(type(edad))
