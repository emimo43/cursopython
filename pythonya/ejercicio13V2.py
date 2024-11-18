'''
    Ejercicio 13.- Se ingresa por teclado un numero positivo de uno o dos digitos (1.99) Mostrar un mensaje indicando si el numero tiene uno o dos digitos (Tener en cuenta que condicion debe cumplirse para tener dos digitos un numero entero)
'''

# Solicitamos un numero entero (positivo al Usuario)
numero = int(input("Favor ingresar un numero entero: "))

# Ingresamos a la condicion if para ver que esta se cumple
if numero < 0:
    print("Favor ingresar un numero positivo")
elif numero > 0 and numero < 10:
        print(f"EL numero {numero} contiene un digito")
elif numero >= 10 and numero < 100:
            print(f"El numero contiene dos digitos")
else:
    print("Favor ingresar un numero correcto")            