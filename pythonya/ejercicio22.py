"""
Ejercicio 22:
Se ingresan por teclado tres numeros, si todos los valores ingresados son menores a 10, imprimir en pantalla la leyenda 'Todos los numeros son menores a diez'"""

# Solicitamos los datos al Usuario
num1 = int(input("Favor ingrese el primer numero: "))
num2 = int(input("Favor ingrese el segundo numero: "))
num3 = int(input("Favor ingrese el tercer numero: "))

# Ingresamos al ciclo if
if(num1 < 10 and num2 < 10 and num3 < 10):
    print("Todos los numeros son menores a diez")