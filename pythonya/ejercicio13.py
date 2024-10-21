'''
    Ejercicio 13 --> Se ingresa por teclado un numero positivo de uno o dos digitos (1..99) Mostrar un mensaje indicando si el numero tiene uno o dos digitos
'''

# Solicitamos los datos al Usuario
numero = int(input("Favor ingresar un numero positivo: "))

# Ahora ingresamos a la condicion if para ver las condiciones
if numero > 0 and numero < 10:
    print(f"El numero {numero} contiene solo un digito\nFin del programa")
else:
    if numero >= 10 and numero < 100:
        print(f"El numero {numero} contiene dos digitos\nFin del programa")
    else:
        print("Favor ingresar un numero positivo de uno o dos digitos")    