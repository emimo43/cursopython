# Strings
print("Hola Mundo") # Esto es un String directo en la impresion

cadena = "Esto es un ejemplo de cadena te texto"
print(cadena) # El String puede ser con comilla doble o simple

cadena = 'Esto es un "ejemplo" de cadena de texto'
print(cadena) # Aqui tenemos comillas dobbles dentro de las comillas simples para resaltar una parte del texto

# Escapar caracter -> String literal en Python
cadena = "Esto es un \"ejemplo\" de cadena de texto"
print(cadena) #  Estas barras invertidas le dicen a Python que pase por alto esas comillas dobles y las muestre por consola para que reslte el texto, tambien puede realizarse con comillas imples

cadena = 'Esto es un \nejemplo de \ncadena de texto'
print(cadena) # El caracter de escape \n permite realizar un salto de linea

cadena = 'Esto es un \tejemplo de cadena de texto'
print(cadena) # El caracter \t es un tabulador

cadena = "Esto es un \bejemplo de cadena de texto"
print(cadena) # El caracter \b quita el espacio con el texto anterior

cadena = "Esto es un \fejemplo de cadena de texto"
print(cadena) # El caracter \f deja el simbolo femenino antes del texto

cadena = "Esto es un ejemplo de \rcadena de texto"
print(cadena) # El caracter \r o retorno de carro suprime texto

cadena = 'Esto es un ejemplo de \vcadena de texto'
print(cadena) # El caracter \v nos muestra por consola el simbolo masculino