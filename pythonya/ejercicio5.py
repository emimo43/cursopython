'''
    Ejercicio 5 --> Realizar la carga del lado del cuadrado, mostrar por pantalla el perimetro del mismo (El perimetro de un cuadrado se calcula multiplicando el valor del lado por cuatro) 
'''

# Lo primero que debemos hacer es solicitar los datos al Usuario
lado = int(input("Favor ingresar el valor del lado del cuadrado: "))

# Ahora creamos una variable llamada perimetro, con la cual podemos resolver la solicitud que nos piden
perimetro = lado * 4

# Ahora mostraremos por pantalla el resultado
print(f"El perimetro del cuadrado es: {perimetro}")