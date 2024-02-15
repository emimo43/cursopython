'''
Problema:
    Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el numero es positivo, negativo o nulo(es decir cero)
'''
# Solicitamos los datos al Usuario
numero = int(input("Favor ingresar un numero entero: "))

# Ahora ingresamos a la condicion if
if numero == 0:
    print(f"El numero ingresado es cero -> {numero} es decir valor nulo")

else:
    if numero > 0:
        print(f"El numero ingresado -> {numero} es positivo")   
    
    elif numero < 0:
        print(f"El numero ingresado -> {numero} es negativo")     
        
print("")
print("Fin del Programa")        