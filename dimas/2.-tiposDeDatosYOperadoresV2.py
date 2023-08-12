#Capitulo2: Variables, tipos de datos y operadores aritmetivos
"""Esto es
un comentario en Varias lineas
"""
#Variables
#Tipos de datos numericos

numero_uno = 1
print(numero_uno)#IMprime la variable
print("numero_uno")#Imprime solo texto

numero_entero = 1
print(numero_entero)

numero_decimal = 2.46
print(numero_decimal)

numero_entero = numero_entero + 2 #Aqui sumamos el valor que tenia el numero entero + s
print(numero_entero)

numero = numero_entero + numero_decimal #Aqui sumamos un numero entero a un numero decimal
print(numero)

numero_entero += 2 #Esto es lo mismo que numero_entero = numero_entero + 2
print(numero_entero)

variable_numerica = 20
variable_numerica = variable_numerica - 10#Aqui restamos
print(variable_numerica)

variable = 10
variable = variable / variable_numerica
print(variable)

numero =  2 / 2 + 3
print(numero)

multiplicacion = 2 * 3
print(multiplicacion)
multiplicacion = numero_entero * numero_decimal
print(multiplicacion)

potencia = 2 ** 3
modulo = 11 % 2
print(potencia)
print(modulo)

# Tipos de Datos: Texto
texto = "Esta es nuestra frase"


text = "Texto 'entre comillas' guay"
textt = 'Texto "entre comillas" guay'
txt = 'Hola'
print(texto)
print(text)
print(textt)
print(txt)

texto_con_formato = """Esto es un texto
 con formato
"""
print(texto_con_formato)