'''
    Ejercicio 1.- Imprime esta frase en la consola "Estoy en el dia 1 del reto de Python"
'''
#print("Estoy en el dia 1 del reto de Python")

# Ejercicio 2.- Almacena el texto anterior en una variable
#reto = "Estoy en el dia 1 del reto de Python"

# Ejercicio 3.- Imprime el valor de la variable anterior
#print(reto)

# Ejercicio 4.- Obvserva estas variables

a = "rojo"
b = "naranja"
c = "azul"
d = "verde"

# Ejercicio 5.- ¿Podrías asignar el valor "verde" a la variable "a" sin escribir "verde"? Imprime el valor de "a" con el valor "verde"
'''
a = d
print(f"El color de a es: {a}")
print(d)
'''
'''
    Ejercicio 6.- Ahora quiero que hagas el siguiente reto.
    ¿Podras hacerlo sin ver las soluciones?
    Debes asignar el valor "rojo" a la variable "c", sin asignar directamente "a" sobre "c".
    Es decir, no puedes hacer esto: c = a.
    Tampoco se permite escribir el valor literalmente
'''
'''
d = a # Estamos asignando el color rojo a la variable d, mostremos por consola
print(a)
print(d)
# Ahora que la variable d tiene el color rojo, se la asignaremos a la variable c, y lo mostramos por consola
c = d
print(c)
'''
# Ejercicio 7.- ¿Es correcta la siguiente instruccion?
'''
frase_1 = "Esta es la primera frase"; frase_2 = "Esta es la segunda frase"
print(frase_1,frase_2)
# Es correcta la instruccion, pero a la vez es mala practica
'''

'''
    Ejercicio 8.- LO siguiente pregunto, es para que apliques el sentido comun, para que digas lo que piensas. ¿Hay algun error aqui? o ¿Es solo estetico?
'''
#print(            "¡Que print mas raro!")

'''
    Ejercicio 9.- ¿Como sacarias estos dos strings (texto) juntos en el print() Si ves que aparecen mal los espacios entre cada frase, arreglalo
'''
'''
frase_1 = "Me llamo Sandra"
frase_2 = "y tengo 23 años"
print(frase_1,frase_2) # Concatenamos con la coma
'''