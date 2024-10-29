'''
        Programación Fácil

    Proyecto y ejercicios – 100 días de Python #1
    
    Ejercicio 1.-
    1.-Imprime esta frase en la consola -> <<Estoy en el dia 1 del reto de Python>>      
    2.-almacena el texto anterior en una variable
    3.-imprime el valor de la variable
    4.- Tenemos 4 variables. Presta atencion a sus valores. En este ejercicio, no tienes que hacer nada
    a = "rojo"
    b = "naranja"
    c = "azul"
    d = "verde"
    5.- ¿Podrias asignar el valor <<verde>> a la variable <<a>> sin escribir <<verde>> Imprime el valor de <<a>> con  el valor <<verde>>
    6.- Ahora, quiero que hagas el siguiente reto. ¿Podrás hacerlo sin ver las soluciones? Debes asignar el valor «rojo» a la variable «c», sin asignar directamente «a» sobre «c». Es decir, no puedes hacer esto: c = a. Tampoco se permite escribir el valor literalmente.
    7.- ¿Es correcta la siguiente instrucción?
    frase_1 = "Esta es la primera frase"; frase_2 = "Esta es la segunda frase"
    8.- La siguiente pregunta es para que apliques el sentido común, para que digas lo que piensas. ¿Hay algún error aquí? ¿O es solo estético?
    print            (         "¡Qué print más raro")
    9.- ¿Cómo sacarías estos dos strings (texto) juntos en el print()? Si ves que aparecen mal los espacios entre cada frase, arréglalo.
    frase_1 = "Me llamo Sandra"
frase_2 = "y tengo 23 años."

print()
10.- Proyecto final del día 1
Es el momento de poner en práctica todo lo aprendido en el día de hoy con un mini proyecto.

Debes construir un programa que haga lo siguiente:

* Frase de saludo inicial.
* Entrada del usuario preguntando el nombre.
* Entrada del usuario preguntando la edad.
* También, una entrada del usuario preguntando el país de nacimiento.
* Comentarios en cada sección del código (tú pon donde creas necesario, no temas equivocarte aquí).
* Vas a tener que presentar los datos recogidos del usuario e imprimirlos en una frase final.
* Debes utilizar saltos de línea en todo el código, donde consideres necesario para que todo quede lo   mejor presentado posible en la consola.
'''
# Soluciones al ejercicio
# 1.-
print("Estoy en el dia 1 del reto de Python")

# 2.-
texto = "Estoy en el dia 1 del reto de Python"

# 3.-
print(texto)

# 4.-
a = "rojo"
b = "naranja"
c = "azul"
d = "verde"

# 5.-
#a = d # Aqui estamos asignando el valor verde que esta en la variable d a la variable a
# Ahora vamos a imprimir la variable a, la cual debe mostrar el color verde
#print(a) # Comentamos esta linea para seguir con el ejercicio

# 6.-
b = a # Aqui para no pasar directo el color rojo a la variable c, se lo pasamos a b, y ahora se lo asignamos a la variable c desde b
# Mostramos por pantalla el valor de b
print(b)
c = b
# Ahora vamos a imprimir la variable c
print(c)

# 7.-
frase_1 = "Esta es la primera frase"; frase_2 = "Esta es la segunda frase"
print(frase_1,frase_2) # Si esta correcta

# 8.-
print(                                    "¡Qué print mas raro")
# Es solo estetico, debido a que imprime solo un espacio fuera de sangria

# 9.-
frase_1 = "Me llamo Sandra"
frase_2 = "y tengo 23 años"
print(frase_1,frase_2) # Se juntan las dos variables separadas por coma

