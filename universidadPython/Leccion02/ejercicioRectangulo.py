'''Instrucciones de la tarea:
- En el siguiente ejercicio se solicita calcular el area y el perimetro de un Rectangulo, para ello debemos crear las siguientes variables:
alto (int)
ancho (int)
- El usuario debe proporcionar los valores de largo y ancho, y despues se debe imprimir el resultado en el siguiente formato

Proporciona el alto: 
Proporciona el Ancho: 
Area: <area> 
Perimetro: <perimetro> 

Las formulas para calcular el area y el perimetro de un Rectangulo son:
Area: alto * ancho
Perimetro: (alto + ancho) * 2
'''

# Creamos las variables y solicitamos los datos al Usuario
alto = int(input("Proporciona el alto del Rectangulo: "))
ancho = int(input("Proporciona el ancho del Rectangulo: "))

# Ahora realizamos los calculos para obtener los datos necesarios
area = alto * ancho
perimetro = (alto + ancho) * 2

# Ahora mostramos por consola el resultado
print(f"Area: {area}")
print(f"Perimetro: {perimetro}")