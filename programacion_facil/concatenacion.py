# En esta clase veremos la concatenacion en Python
fragmento1 = "La programacion es como la vida "
fragmento2 = "llena de errores, pero tambien de posibilidades"
espacio = " "

# Ahora mostramos por consola el resultado de la concatenacion
frase_completa = fragmento1 + fragmento2
print(frase_completa)
print(type(frase_completa))
# Otra forma de mostrar en pantalla es añadiendole un string
frase_completa = fragmento1 + " " + fragmento2
print(frase_completa)
# Otra manera de concatenar es todo en un print
print("La programacion es como la vida: " + "llena de errores, pero tambien de posibilidades")