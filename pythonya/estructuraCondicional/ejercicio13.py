"""Problema: Se ingresa por teclado un numero positivo de uno o dos digitos(1.99) mostrar un mensaje indicando si el numero tiene uno o dos digitos (Tener en cuenta que condicion debe cumplirse para tener dos digitos un numero entero)"""

# Solicitamos los datos al usuario
numero = int(input("Favor ingresar un numero entero: "))

# Ahora veremos la condicion if
if(numero > 0):
    if(numero < 10):
        print("El numero tiene un digito")
    elif(numero >= 10 and numero < 100):
        print("El numero tiene dos digitos") 
    elif(numero > 100):
        print("El numero tiene mas de dos digitos")    
else:
    print("El numero esta fuera del rango")