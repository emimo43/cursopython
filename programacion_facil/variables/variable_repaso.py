# Repaso de variables en Python

edad = 28
print(edad)

numero_1 = 10
print(numero_1)
print(type(numero_1)) # Mostrara el tipo de dato, en este caso es un entero

numero_1 = "Hola"
print(numero_1)
print(type(numero_1)) # Ahora nos mostrara el tipo de dato que es un str

# Reasignacion de variables en Python, esto significa que le vamos cambiando el tipo de dato

edad = 20
print(edad)

edad = 32
print(edad)

edad = 26
print(edad)

'''
   En Python hay un elemento especial llamado None. Este elemento se utiliza normalmente para dejar una variable declarada, “sin inicializar”.

Con None, indicaremos que queremos que la variable contenga un valor nulo o “vacío”. No obstante, aunque sea un valor nulo, realmente estamos inicializándola con un valor. 
'''
numero_1 = None
print(numero_1)

'''
    Inicializar variables con tipo de dato
Python no deja tener las variables vacías, pero podemos dejarlas inicializadas con un tipo de dato concreto. Por ejemplo, que queremos una variable para guardar valores numéricos enteros (int), pero aún no queremos poner ningún valor concreto. Entonces, se puede hacer esto:
'''
numero_1 = int()

'''
    Con esto creamos una variable de tipo int, pero no la inicializamos con un número concreto.

No obstante, esto lo que hace es inicializar con un valor 0. Si imprimes la variable en la consola, lo verás:


'''
print(numero_1) # Este valor 0 sera sustituido despues en al reasignar un valor diferente a la variable

'''
    Asignación múltiple
En Python puedes declarar varias variables de una sola vez, y asignarles valores en una misma instrucción o línea de código. La sintaxis es la siguiente:
'''
numero_1,numero_2,numero_3 = 10,12,17
print(numero_1,numero_2,numero_3)

numero_1 = 20
print(numero_1)