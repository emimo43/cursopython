'''
    En este capitulo veremos los tipos de datos en Python
'''

'''
    Los datos de tipo str se utilizan para representar texto
    El nombre de este tipo de dato proviene de string que se traduce al español como cadena de caracteres
'''

'''
    Consejo 1.- Usa enteros int para contar elementos o realizar calculos sin decimales, utiliza cadenas str para manejar texto, numeros de punto flotante float para calculos con decimales, y valores booleanos bool para reprenstar condiciones verdaderas o falsas
'''

'''
    Consejo 2.- Python permite cambiar entre tipos de datos de manera sencilla, si quieres que una variable sea de un tipo concreto, simplemente añadele un valor de ese tipo
'''

'''
    Una cadena de caracteres es un conjunto de letras, numeros, o simbolos que comunmente llamamos "texto"
    Puedes crear una variable de este tipo asignando texto entrecomillado
    Por ejemplo
'''
saludo = "Hola Mundo"

'''
    Al entrecomillar el texto le indicamos al intérprete de Python donde empieza y donde acaba. Las primeras comillas indican la apertura de la cadena de caracteres, y las otras, indican el cierre. Si el intérprete de Python no encuentra el cierre, se produce un error.
    De ahora en adelante, me referiré a este tipo de dato como str, cadena de texto, cadena de caracteres o string.

    Todos estos nombres son para referirse a lo mismo, y se emplean muy a menudo por la comunidad de programadores.
    
    Las cadenas de caracteres se pueden escribir tanto con las comillas simples (''), como con comillas dobles ("").

    Aquí tienes el ejemplo anterior, escrito con comillas simples. Perfectamente válido, también.

'''
saludo = 'Hola Mundo'

'''
    El tipo de dato numérico entero (int)
    El tipo de dato int se utiliza para almacenar números enteros. Es decir, números positivos, negativos y cero. Sin decimales.

    Puedes crear una variable de tipo int, simplemente asignando sin comillas, un valor numérico entero a una variable. Por ejemplo:
'''
edad = 32

'''
    Para representar un número negativo, lo haremos añadiendo el símbolo menos (-) junto al número, y sin espacios:
'''
temperatura = -10

'''
    El término integer se traduce al español como entero.

    El tipo de dato int proviene de este término.
    
    Recuerda poner siempre los valores numéricos sin comillas, si no, serán simple texto con el que no podremos hacer operaciones matemáticas con normalidad.
'''

'''
    El tipo de dato decimal (float)
    Los números de punto flotante, conocidos como float, se utilizan para representar números con decimales.

    Puedes crear una variable de este tipo, asignando, sin comillas, un valor numérico con decimales a una variable.
    Pueden ser números positivos, cero o negativos, pero siempre con parte decimal. Si los pones sin parte decimal, serán interpretados por el intérprete de Python, como tipo de dato int.

    Este tipo de dato se conoce como número de punto flotante, número de coma flotante o simplemente, decimales.

    Número de punto flotante, se dice en inglés floating point number.

    Decimales, se dice decimals.
    Aquí tienes un ejemplo de un tipo de dato float:
'''

PI = 3.14159

'''
    ¡Importante! La parte decimal de los datos de tipo float debe ir con un punto, no una coma.

    Si quieres crear un float negativo, añádele el símbolo menos (-) antes del número:
'''
valor_negativo = -17.6743

'''
    El tipo de dato booleano (bool)
    Los datos de tipo bool de Python, se utilizan para representar valores booleanos.

    Estos valores booleanos únicamente tienen dos posibles estados: True y False (verdadero y falso).

    Para crear una variable de este tipo, solo tienes que asignarle uno de estos dos valores sin comillas, para evitar que sean tratados como tipo de dato str.

    Aquí tienes un ejemplo con las dos posibilidades de este tipo de dato:
'''
valor_booleano = True
valor_booleano = False

'''
    ¡Importante! El intérprete de Python distingue mayúsculas de minúsculas. Por lo tanto, ten en cuenta que la T y la F, de True y False, respectivamente, deben ir siempre en letra mayúscula. El resto, en letra minúscula.
    
    Booleano en inglés se dice boolean.

    El tipo bool, proviene de ese nombre.
    
    Los booleanos vienen del álgebra de Boole, un sistema algebraico desarrollado por el matemático británico George Boole en el siglo XIX.
'''
# Ejercicios de Python para resolver

# 6.- ¿Sabrias decir de que tipo de dato es cada uno de los siguientes datos?

# A. "True"
print(type("True"))

# B. False
print(type(False))

# C. 10.0
print(type(10.0))

# D. -50
print(type(-50))

# E. "Curso de Python"
print(type("Curso de Python"))

# 7.- De los siguientes datos ¿Cuales produciran errores y cuales no? Indica si la sintaxis es correcta o no, y en que te basas para deducirlo

# A. "false"
print(type("false"))
# B. 10
print(type(10))

# C. 656.504.3 -> Esta manera esta incorrecta
print(type(656_504_3)) 

# D. 50.54
print(type(50.54))

# E. False
print(type(False))

# F. "Aprendiendo Python"
print(type("Aprendiendo Python"))