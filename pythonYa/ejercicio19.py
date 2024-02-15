'''
Problema:
    Confeccionar un programa que lea por teclado tres numeros enteros distintos y nos muestre el mayor
'''
# Solicitamos los datos al Usuario
numero1 = int(input("Favor ingrese el primer numero entero: "))
numero2 = int(input("Favor ingresar el segundo numero entero: "))
numero3 = int(input("Favor ingrese el tercer numero entero: "))

# Ingresaos a la sentencia condicional if
if numero1 > numero2 and numero1 > numero3:
    print(f"El numero 1 -> {numero1} es el mayor")
elif numero2> numero1 and numero2 > numero3:
    print(f"El numero 2 -> {numero2} es el mayor")
else:
    print(f"El numero 3 -> {numero3} es el mayor")      
    
print("")
print("Fin del Programa")      