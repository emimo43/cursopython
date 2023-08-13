# Declaracion Multiple (variables)

a,b,c = 5,3,2

print(a)
print(b)
print(c)
print(a,b,c)

# Otra forma de declaracion multiple es la siguiente solicitando los datos al usuario
print("Deme 3 valores")
x,y,z = input(),input(),input() # Aqui ingresaremos los tres valores por teclado
suma = int(x) + int(y) + int(z) # Aqui sumamos las 3 variables, se debe castear esta operacion, debido a que lo que ingresamos son datos de tipo string, se deben castear por separado
print("La suma de los 3 numeros es:",suma) # Aqui mostramos por consola el resultado de la operacion