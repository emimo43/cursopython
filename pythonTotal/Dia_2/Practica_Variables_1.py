'''
    Práctica con Variables 1
    Declara dos variables, llamadas nombre y edad.

    Asigna a la variable nombre el valor "Tony Soprano", y a la edad, el valor 51.
'''
# Declaramos las variables
nombre = "Tony Soprano"
edad = 51
print(nombre)
print(edad)

'''
    Práctica con Variables 2
    Crea tres variables:
1. nombre
2. apellido
3. nombrecompleto
A nombre, asígnale el valor "Julia", y en apellido, asigna el valor "Roberts". Finalmente,
construye la variable nombrecompleto concatenando las variables
(recuerda sumar un espacio intermedio).
'''
# Creamos las variables
nombre = "Julia"
apellido = "Roberts"
nombrecompleto = nombre + " " + apellido
print(nombrecompleto)

'''
    Práctica con Variables 3
    Declara la variable curso, asígnale el valor "Python", y muestra en pantalla la frase:
    Estás tomando un curso de curso
    Para ello deberás concatenar la primera parte de la frase con el valor que asumirá la variable.
     Recuerda agregar un espacio antes de concatenar la variable al resto del texto.
'''
# Declaramos la variable
curso = "Python"
print("Estás tomando un curso de " + curso)
print(f"Estás tomando un curso de {curso}")