""" Se cargan por teclado tres numeros distintos. Mostrar por pantalla el mayor de ellos"""
# Solicitamos los datos al usuario
print("Favor ingresar el primer numero: ")
numero1 = int(input()) # Aqui casteamos el str a int
print("Favor ingresar el segundo numero: ")
numero2 = int(input())
print("Favor ingrese el tercer numero: ")
numero3 = int(input())

# Ahora comenzamos a realizar el ciclo y condicionales para ver cual es el numero mayor
if(numero1 > numero2 and numero1 > numero3):
    print(f"El numero mayor es:{numero1}")
else:
    if(numero2 > numero1 and numero2 > numero3):
        print(f"El numero mayor es: {numero2}")
    else:
        print(f"El numero mayor es: {numero3}")