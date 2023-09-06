"""Se ingresan por teclado tres numeros, si todos los valores ingresados son menores a 10, imprimir en pantalla la leyenda "Todos los numeros son menores a diez"""

# Solicitamos los datos al Usuario
numero1 = int(input("Favor ingresar el primer numero: "))
numero2 = int(input("Favor ingresar el segundo numero: "))
numero3 = int(input("Favor ingresar el tercer numero: "))

# Ahora generamos las condiciones para realizar la operacion
if(numero1 < 10 and numero2 < 10 and numero3 < 10):
    print('"Todos los numeros son menores a diez"')