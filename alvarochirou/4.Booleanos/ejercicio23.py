"""
Ejercicio 23: Se ingresan por teclado tres numeros, si al menos uno de los valores ingresados es menor a 10, imprimir en pantalla la leyenda 'Alguno de los numeros es menor a diez"""

# Solicitamos los datos al Usuario
num1 = int(input("Favor ingrese el primer numero: "))
num2 = int(input("Favor ingrese el segundo numero: "))
num3 = int(input("Favor ingrese el tercer numero: "))

# Ingresamos al ciclo if
if(num1 < 10 or num2 < 10 or num3 < 10):
    print("Alguno de los numeros es menor a diez")