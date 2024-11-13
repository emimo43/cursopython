# Para que en un texto salgan comillas dentro de un string, se hace de la siguiente manera

'''
print("'Blue' es azul en español") # Aqui lo hago con comillas simples
print('"Blue" es azul en español') # Aqui lo hago con comillas dobles

# Ahora veremos la funcion len() la cual devuelve la cantidad de string que estan en una frase
# Un dato literal es un valor escrito literalmente
print(len("Amarillo")) # Nos indica que tiene 8 posiciones

# AHora veremos este metodo usando una variable
color = "Amarillo"
print(len(color))

# Posiciones de String -> Se cuenta desde el cero
print(color[0]) # La posicion 0 corresponde a la letra A

# El tipo de dato integer

numero_1 = 100
numero_2 = 400

print(numero_1 + numero_2) # Esto es una suma en python

# Los numeros en String con el signo + es una concatenacion
resultado = numero_1 + numero_2
print(resultado)
resultado = numero_1 - numero_2
print(resultado)
resultado = numero_1 * numero_2
print(resultado)
resultado = numero_1 / numero_2
print(resultado)
resultado = numero_1 // numero_2 # Esto es una division entera
print(resultado)

# Calculo de exponentes
print(2**10)
'''

# Operaciones aritmeticas con parentesis
'''
operacion_1 = 10 + 56 * 89 - 3 / 2
operacion_2 = 10 + 56 * (89 -3) / 2

print(operacion_1)
print(operacion_2)

# Separadores en numeros muy largos, en Python se usan guiones bajos, y estos son ignorados al imprimir en consola
numero_1 = 4_897_567_800_678_543_558
print(numero_1)

# Tipos de datos, conversiones, operadores y mas -> Python en 100 dias -> Dia 2

print('"Blue es azul en español"')

# La funcion len() indica cuantos caracteres trae un String
print(len("Amarillo")) # Nos indica que trae 8 caracteres

# Si quieremos saber cuantos caracteres trae una variable con la funcion len() se hace de la siguiente forma
color = "Amarillo"
print(color)
print(len(color))

# Posiciones en los String, siempre se cuenta desde cero, esto se indica con []
print(color[0]) # Nos debe indicar que es la posicion 0, esta le letra A, debemos ingresar en los corchetes el 0

# Los integer
numero_1 = 100
numero_2 = 400
print(numero_1 + numero_2)

numero_11 = "100"
numero_22 = "400"
print(numero_11 + numero_22) # Aqui estamos concatenando dos String

resultado = numero_1 + numero_2
print(resultado) # Aqui almaceno la suma de los dos integer

resultado = numero_1 - numero_2
print(resultado)

resultado = numero_1 * numero_2
print(resultado)

resultado = numero_1 / numero_2
print(resultado)

resultado = numero_1 // numero_2 # Division entera
print(resultado)

# Calculo de exponentes -> **
print(2 **10)

# Tipos de datos Float

# Como ver el tipo de dato en Python -> Esto se realiza con la funcion type()

numero_1 = 4
numero_2 = 769.97
texto = "Soy un  string."
decision = True

# Ahora mostramos en consola el tipo de dato
print(type(numero_1)) # int
print(type(numero_2)) # float
print(type(texto)) # str -> string
print(type(decision)) # bool

# Numeros en la funcion len() -> Funciona con strings, si utilizamos con ella numeros, nos va a dar un error
numero = 897860654565

print(len(numero)) # En este caso nos indica error, por que la variable numero no tiene string, si no un dato int -> Para contar los caracteres de un numero se debe dejar como String

numero = "877890654565"
print(len(numero)) # Ahora si mostrara la cantidad de caracteres por ser un String
'''

'''
    Transformar integer en string -->
    Tenemos disponible la funcion str() que transforma un valor string

numero = 897890654565 # Esta variable es de tipo int

digitos = str(numero) # En la variable digitos almacenamos lo que tiene la variable numero, pero ahora lo convertimos en str, con la funcion str()

print(len(digitos)) # A la variable digitos ya convertida en str, veremos cuantos caracteres tienen con la funcion len()


# Conversion de string a int
# Declaramos las varibles

numero_1 = "10"
numero_2 = "50"

# Creamos la variable suma para guardar el dato ya convertido a int y tener el valor de la suma
numero_1 = "10"
numero_2 = "50"

suma = int(numero_1) + int(numero_2)

print(suma) # El metodo int() debe ir en ambos numeros


# Transoformar datos a Float
numero_1 = "10.57"
numero_2 = "50.9"

# Estas dos variables son de tipo string, ahora las vamos a convertir a tipo float o sea de numero real
suma = float(numero_1) + float(numero_2)

# Ahora mostramos por consola el resultado
print(suma)

# Redondeo de numeros
multiplicacion = 7.5678 * 6.943534
print(round(multiplicacion)) # La funcion round() nos redonde la cifra

# Por si no lo sabes lo que es un redondeo, aqui tienes algunos ejemplos
print(round(7.3))
print(round(7.5))
print(round(7.7))


    round() permite añadir un segundo argumento aparte del valor. Le indicaran la cantidad de decimales que quieres

print(round(multiplicacion,2)) # El dos indica la cantidad de decimales que tendra la variable
'''
'''
El operador de floor division -> Este operador // realiza divisiones y redondea el resultado al valor entero mas cercano, veamos una division primero
'''

#division = 10/3
#print(division) # El resultado es 3.33333333333

# Ahora, hagamos la misma division, pero con el nuevo operador
#division = 10 // 3 # Ahora nos dara una division exacta
#print(division)

# Operador Modulo

'''
    Este operador modulo(%) realiza tambien la division, pero en lugar de devolvernos el resultado, nos devuelve el resto
'''

#division = 10 % 3
#print(division) # El resultado es 1

'''
    Truncamiento de numeros -> Podemos realizar un truncamiento de numeros convirtiendo tipos de datos. En el siguiente codigo tenemos dos numeros decimales. SI realizamos una operacion con ellos, nos devuelve un valor decimal, aunque sea 0
'''
#numero_1 = 10.60
#numero_2 = 10.40

#suma = numero_1 + numero_2

#print(suma)

'''
    Si transformamos el valor del resultado a int() vamos a truncar los decimales, ya que el tipo de dato se convierte en integer y no admite decimales, los perdemos. Esto es util cuando solo quieres valores enteros
'''
'''
numero_1 = 10.60
numero_2 = 10.40

suma = numero_1 + numero_2

trunca_suma = int(suma) # Aqui estamos convirtiendo el valor float a integer

print(trunca_suma)
# Corroboramos esto con la funcion type()
print(type(trunca_suma))
'''

'''
    Redondeo de numeros --> En Python tenemos una funcion util llmada round() la cual, nos va a permitir redondear valores numericos.
    En la siguiente multiplicacion obtenemos muchos decimales
'''
#multiplicacion = 7.5678 * 6.943534
#print(multiplicacion)

# Si utlicamos round() va a redondear a entero, a la alta o la baja, dependiendo de los decimales
#multiplicacion = 7.5678 * 6.943534

#print(round(multiplicacion))

'''
    Por si no sabes que es el redondeo a la alta o a la baja, aqui tienes un ejemplo
    print(round(7.3))
    print(round(7.5))
    print(round(7.7))
    
    Y si no quieremos perder todos los decimales, de dejar unos cuantos?
    
    round() permite añadir un segundo argumento aparte del valor. Le indicaremos la cantidad de decimales que queremos
    
    multiplicacion = 7.5678 * 6.943534
    
    print(round(multiplicacion, 2))
    
    De todas formas, el redondeo lo sigue realizando con los decimales que le quedan
'''

'''
    Operador de asignacion de incremento y decremento -->
    
    Hasta ahora, has visto el operador de asignacion == el que utilizamos para asignar valores a las variables. No obstante, tenemos mas variantes de este operador. Hay muchos, asi que en esta ocacion, solo veremos el incremento y decremento
'''

# Operador +=
# Este operador asigna un incremento determinado a una variable

#numero_1 = 10

#numero_1 += 10 # Incrementa la variable en 10, el resultado sera 10 +10

#print(numero_1) # Resultado es igual a 20 

# Operador -=

# Este operador hace lo contrario que el anterior, decrementa valores a si misma

#numero_1 = 100

#numero_1 -= 25 # Aqui decrementamos el valor 100 en menos 25

#print(numero_1) # El resultado es 75

'''
    Formateo de Strings -->
    Hay una cosa importante que debo detellar antes de continuar con el siguiente capitulo, el formateo de string
'''
suma = 90 + 67 # Estos son tipo de datos int
print("El resultado de la suma es: " + str(suma)) # Aqui convertimos la variable suma a string

# Pero tenemos mejor la funcion f{}
print(f"El valor de la suma es: {suma}")