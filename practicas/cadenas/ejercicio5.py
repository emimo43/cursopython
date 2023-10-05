"""Realizar la carga del lado de un cuadrado, mostrar por pantalla el perimetro del mismo (El perimetro de un cuadrado se calcula multiplicando el valor del lado por el cuatro)"""

def perimetro():
    lado = int(input("Favor ingrese el valor del lado: "))
    valor_lado = lado * 4
    return valor_lado
valor_perimetro = perimetro()

print(f"El valor del perimetro es {valor_perimetro}")