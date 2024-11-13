# Sintaxis de la variable de en Python

edad = 28 # Edad es el identificador y le asignamos un valor en este caso es 28

numero_1 = 10 # Esta variable es de tipo entero -> int

numero_1 = "Hola" # Ahora la variable cambio a tipo str -> string

# A esto le llmamos tipado dinamico

edad = 20
edad = 32
edad = 26
# El ultimo valor es el que queda en la variable -> Esto es la reasignacion de valores

'''
    Declaración e inicialización de variables
Declarar o definir una variable, significa crearla.

Inicializar una variable, significa darle un valor cuando no tiene uno previamente. Es decir, darle un valor inicial.

Declarar sin inicializar variables
En Python, declarar variables sin inicializarlas, no es posible.

Hay otros lenguajes de programación como Java, que sí lo permiten. Así que nos encontramos con una de las cosas que caracterizan a Python.

Si intentas ejecutar el siguiente código, recibirás este error:

numero_1
numero_1 = 10
Python
   Error en la consola
NameError: name 'numero_1' is not defined.
Error de nombre: el nombre 'numero_1' no está definido.
El error ocurre en la primera línea. Nos indica que el nombre de la variable no está definido. Claro, eso es lo que intentamos hacer al escribir su nombre, definir la variable, y luego, en la segunda línea, se intenta inicializar con un valor. No obstante, el intérprete ni siquiera llega a ejecutar la segunda línea. Ha fallado en la primera.


'''
numero_1 = 10 # Esto si es correcto al definir la variable

'''
    En Python hay un elemento especial llamado None. Este elemento se utiliza normalmente para dejar una variable declarada, “sin inicializar”.

Con None, indicaremos que queremos que la variable contenga un valor nulo o “vacío”. No obstante, aunque sea un valor nulo, realmente estamos inicializándola con un valor.
'''
numero_1 = None

'''
    Inicializar variables con tipo de dato
Python no deja tener las variables vacías, pero podemos dejarlas inicializadas con un tipo de dato concreto. Por ejemplo, que queremos una variable para guardar valores numéricos enteros (int), pero aún no queremos poner ningún valor concreto. Entonces, se puede hacer esto:
'''
numero_1 = int()

'''
    Con esto creamos una variable de tipo int, pero no la inicializamos con un número concreto.

No obstante, esto lo que hace es inicializar con un valor 0. Si imprimes la variable en la consola, lo verás:
'''
numero_1 = int()

#print(numero_1) # Resultado en la consola sera 0 -> Este valor 0 será sustituido después en al reasignar un valor diferente a la variable.

'''
    Asignación múltiple
En Python puedes declarar varias variables de una sola vez, y asignarles valores en una misma instrucción o línea de código. La sintaxis es la siguiente:

a, b, c = valor_a, valor_b, valor_c
Sintaxis
Aquí tienes un ejemplo de uso:
numero_1, numero_2, numero_3 = 10, 12, 17
Python
En este ejemplo se va a asignar el valor 10 a la variable numero_1, el valor 12 a la variable numero_2, y el valor 17 a la variable numero_3.
En caso contrario recibirás el siguiente error:

numero_1, numero_2, numero_3 = 10
Python
 Error en la consola
TypeError: cannot unpack non-iterable int object
Error de tipo: no es posible desempaquetar el objeto no iterable de tipo int
'''

'''
    Imprimir valores de variables en la consola
Para imprimir el valor de una variable en la consola, en Python lo hacemos con la función predefinida print().

Entre sus paréntesis, llamamos a la variable con su nombre:
'''
numero_1 = 10
print(numero_1) # EL resultado de la consola es 10

'''
    Reasignar valores a variables
Para darle un valor nuevo a una variable que ya tiene otro (reasignar), lo hacemos con la misma sintaxis que la declaración.

En el siguiente ejemplo, primero declaro la variable numero_1 con un valor de 10, y en la siguiente línea le reasigno un valor de 20.


'''
numero_1 = 10
numero_1 = 20
print(numero_1) # Resultado en la consola 20

'''
    Como he explicado, las variables solo pueden tener un valor a la vez. Sin embargo, es posible usar el valor que tiene una variable tantas veces como se desee antes de reasignarle un nuevo valor.

Por ejemplo:

numero_1 = 10
print(numero_1)

numero_1 = 20
print(numero_1)
Python
   Resultado en la consola
10
20

En la primera línea se declara e inicializa la variable numero_1 con un valor 10.
En la segunda línea se imprime (utiliza) el valor de dicha variable. Aparecerá en la consola el valor 10.
En cuarta línea se reasigna la variable con el valor 20. Esta vez, en el último print() (línea 5), aparecerá el valor 20.
'''
