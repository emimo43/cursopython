"""Ejercicio 19:
Problema: Confeccionar un programa que lea por teclado tres numeros enteros distintos y nos muestre el mayor."""

# Solicitamos los datos al usuario
numero1 = int(input("Favor ingrese el primer numero entero: "))
numero2 = int(input("Favor ingrese el segundo numero entero: "))
numero3 = int(input("Favor ingrese el tercer numero entero: "))

# Ahora generamos la condicion if para ver cual es el numero mayor
if(numero1 > numero2 and numero1 > numero3):
    print(f"El primer numero que es el {numero1} es el mayor")
else:
    if(numero2 > numero1 and numero2 > numero3):
        print(f"El segundo numero que es el  {numero2} es el mayor")
    else:
        print(f"El tercer numero que es el {numero3} es el mayor")