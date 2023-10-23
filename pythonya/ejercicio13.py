"""Ejercicio 13: Se ingresa por teclado un numero positivo de uno o dos digitos (1..99) Mostrar un mensaje indicando si el numero tiene uno o dos digitos"""

# Solicitamos los datos al Usuario
numero = int(input("Favor ingrese un numero positivo: "))

# Ingresamos a la condicion IF
if(numero >= 1 and numero < 10):
    print("El numero contiene un digito")
else:    
    if(numero >= 10 and numero < 100):
        print("El numero contiene dos digitos")
     