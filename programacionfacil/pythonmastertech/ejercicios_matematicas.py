# Ejercicios de Python para resolver de Matematicas

# 11.- Realiza las siguientes operaciones en diferentes variables(una variable para cada operacion) Despues imprime el resultado de todas ellas

# A.- 10 / 2
division = 10 / 2
print(division)

# B.- 6 * 3 + 2
resultado = 6 * 3 + 2
print(resultado)

# C.- 7 + 65
suma = 7 + 65
print(suma)

'''
    12.- Crea tres variables para almacenar un numero en cada una de ellas, y otra para realizar una operacion y almacenar el resultado en ella.
    
    Te voy a poner las operaciones y las tienes que representar con variables. En este ejercicio, no puedes operar con los valores directos.
    
    Estas son las operaciones:

56 * 6548 - 2
6556 + 76 + 45
7 + 65 - 642
Por ejemplo, en la operación del apartado A, 56 irá en una variable, 6548 en otra y 2 en otra. Las operaciones se harán sobre una cuarta variable.

Te dejo un ejemplo de como tienes que estructurar el código para que no haya confusión con el enunciado:

numero_1 = 10
numero_2 = 6
numero_3 = 8
resultado = # Aquí tienes que hacer las operaciones con los nombres de variable
'''
# Inicializamos las variables y les asignamos un valor
numero_1 = 10
numero_2 = 25
numero_3 = 50

resultado = numero_1 * numero_2 - numero_3
print(resultado)

resultado = numero_1 + numero_2 + numero_3
print(resultado)

resultado = numero_1 + numero_2 - numero_3
print(resultado)

# 13.- Calcula 2 elevado a 6
exponente = 2 ** 6
print(exponente)

# Declaramos las variables
base = 2
exponente = 6

# Realizamos la operación
operacion = base ** exponente

# Imprimimos el resultado
print(operacion)

# 14.- Calcula 10 elevado a 10
base = 10
exponente = 10

operacion = base ** exponente
print(operacion)

# 15.- Divide 100 entre 30 y que te devuelva un valor entero
numero = 100
divisor = 30

operacion = 100 // 30 # Esta es una division entera
print(operacion)

# Declaramos las variables
dividendo = 100
divisor = 30

# Realizamos la operación
cociente = dividendo // divisor

# Imprimimos el resultado
print(cociente)

# 16.- ¿Cual es el cociente de 13 dividido por 5 usando la division entera?
# Declaramos las variables
dividendo = 13
divisor = 5

# Realizamos la operacion
cociente = dividendo // divisor
print(cociente)

# 17.- Encuentra el resto de la division de 17 entre 2
# Declaramos las variables

dividendo = 17
divisor = 2

# Realizamos la operacion de modulo
modulo = 17 % 2

# Mostramos por consola el valor solicitado
print(modulo)

'''
En los siguientes ejercicios, simplemente responde, no hace falta que obtengas el resultado. Claro, que si quieres pruébalo con código Python. Así vas practicando.

18. En la operación 10 + 54 + 6 - 2, ¿qué parte se soluciona primero? ¿A, B o C?

10 + 54
54 + 6
6 - 2
Se resuelve primero la parte A, puesto que la suma y la resta están al mismo nivel de prioridad. En este caso, se resuelve la que está primero, de izquierda a derecha.

19. En la operación 80 * 6 / 40 * 2, ¿qué parte se soluciona primero? ¿A, B o C?

80 * 6
6 / 40
40 * 2
Se resuelve primero la parte A, ya que las multiplicaciones y divisiones tienen la misma prioridad. Ocurre igual que en el ejercicio anterior. Se resuelve la que está primero.

20. En la operación 80 * 6 + (40 + 2), ¿qué parte se soluciona primero? ¿A o B?

80 * 6
40 + 2
21. De los siguientes números, ¿sabrías decirme cuáles darían error con el intérprete de Python? Puedes hacer las pruebas que creas convenientes.

678_656
567-688-984
674856587
0.65
567-688-984.743
Las respuestas A, C y D son correctas. El resto no.

En la A, se está empleando una sintaxis correcta, para representar números largos.
En la B, se están utilizando guiones. Esta sintaxis es incorrecta.
En la C, se utiliza un número entero normal y corriente. Esta sintaxis es correcta.
En la D, se utiliza un número decimal con el punto decimal. Esta sintaxis es correcta.
Finalmente, en la E, se están usando guiones en un número decimal. Esta sintaxis es incorrecta (en la parte entera).
'''