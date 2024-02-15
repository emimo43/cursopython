'''
Problema:
    Se ingresa por teclado un numero positivo de uno o dos digitos (1..99) mostrar un mensaje indicando si el numero tiene uno o dos digitos
    (Tener en cuenta que condicion debe cumplirse para tener dos digitos un numero entero)
'''
# Solicitamos los datos al Usuario
numero = int(input("Favor ingrese un numero entero: "))

# Comenzamos la condicion if
if numero >= 0 and numero < 10:
    print(f"El numero {numero} contiene un digito")

elif numero >= 10 and numero < 100:
    print(f"El numero {numero} contiene dos digitos")
    
else:
    print("Favor ingrese un numero correcto")
    
print("Fin del programa")            