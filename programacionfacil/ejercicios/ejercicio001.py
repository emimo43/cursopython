# En este ejercicio veremos variables en Python
'''
a = 4 +4 # Aqui tenemos la variable a que contiene la suma de 4 + 4
b = 4.5 + 4.56

# Ahora mostraremos por consola los tipos de datos que son estas varibales con el metodo type()
print(type(a))
print(type(b))
# Esto nos arrojara que a es de tipo int y b de tipo float
# Ahora vamos a mostrar por consola el resultado con la funcion print y despues creamos la variable resultado para mostrar con una variable el resultado de otra forma
print(a + b)
resultado = a + b
print(f"El resultado de la suma de a y b es: {resultado} ")

# Ahora mostraremos por consola un mensaje tanto en comillas simples como dobles
print("Hola Mundo desde Python")
print("Hola Mundo desde 'Pyhton'")
saludo = "Hola Mundo desde 'Python'"
print(saludo)

# Estos tipos de datos son String, o sea cadena de caracteres

frase_bienvenida = "Primer dia de Python"
print(type)
print(frase_bienvenida)


# Asiganar variables a otras variables
variable_1 = "Hola"
variable_2 = variable_1
print(variable_2) # Esta variable mostrara el Hola que es de la variable_1


# Reasignacion de valores en variables
a = "Este es mi valor inicial"
print(a)

a = "Mi valor ha cambiado" # Ahora tenemos otro valor en la variable a
print(a)

# La funcion es la encargada de ingresar datos al programa
nombre = input("Por favor, introduzca su nombre: ")
print(nombre)

# Ahora lo veremos con el salto de Linea con el parametro \n
nombre = input("Por favor introduzca su nombre\n")
print(nombre)

# Ahora veremos la concatenacion, que es unir String
nombre = input("Por favor introduzca su nombre: ")
print("Bienvenido/a " + nombre + ".")
# Tenemos la opcion de concatenar con f -> Format
print(f"Bienvenido/a {nombre}.") 
'''
# 1.- Imprime esta frase en consola <Estoy en el dia 1 del reto de Python>
#print("Estoy en el dia 1 de Python")

# 2.- Almacena el texto anterior en una variable
#saludo = "Estoy en el dia 1 de Python"

# 3.- Imprime el valor de la variable anterior
#print(saludo)

'''
    4.- Tenemos 4 variables. Presta atencion a sus valores. En este ejercicio, no tienes que hacer nada
    '''
a = "rojo"
b = "naranja"
c = "azul"
d = "verde"

# 5.- ¿Podras asignar el valor <verde> a la variable <a> sin escribir <verde>? Imprime el valor de <a> con el valor <verde>
a = d # Aqui le asignamos a la variabla a el valor de d que es verde
print(a)

# 6.- Ahora quiero que hagas el siguiente reto ¿Podras hacerlo sin ver las soluciones? Debes asiganar el valor <rojo> a la variable <c> sin asignar directamente <a> sobre <c>. Es decir, no puedes hacer esto c = a. Tampoco se permite escribir el valor literalmente

