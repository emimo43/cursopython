'''
    Ejercicio --> 
    
        Instrucciones de la tarea:
        En el siguiente ejercicio se solicita calcular el area y el perimetro de un Rectangulo, para ello debemos crear las siguientes variables:
        
        alto(int)
        ancho(int)
        
        El Usuario debe proporcionar los valores de largo y ancho, y despues debe imprimir el resultado en el siguiente formato
        
        Area : <area>
        Perimetro : <perimetro>
        
        Las formulas para calcular el area y el perimetro de un Rectangulo son:
        
        Area = alto * ancho
        Perimetro = (alto + ancho) * 2
'''
alto = int(input("Favor ingresar el valor alto: "))
ancho = int(input("Favor ingresar el valor del ancho: "))

# Ahora creamos las formulas para obtener los resultados

area = alto * ancho
perimetro = (alto + ancho) * 2

print(f"Area: {area}")
print(f"Perimetro: {perimetro}")