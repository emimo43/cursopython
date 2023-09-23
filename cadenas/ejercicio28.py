# Cortar cadena de texto -> metodo split()

frase = "Hola, Develoteca"
print(frase)
print(frase.split(",")) # -> Aqui con el metodo split() dividiremos usando la coma

frase2 = " Hola: Develoteca"
print(frase2)
print(frase2.split(":")) # Aunque sea dos puntos, igual con este metodo dividira por coma

frase3 = " Hola: Develoteca: Curso de Python"
print(frase3.split())