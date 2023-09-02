"""Se ingresa por teclado tres numeros, si al menos uno de los valores ingresados es menor a 10, imprimir en pantalla la leyenda "Alguno de los numeros es menor a diez"""

# Solicitamos los datos al usuario
numero1 = int(input("Favor ingresar el primer numero: "))
numero2 = int(input("Favor ingresar el segundo numero: "))
numero3 = int(input("Favor ingresar el tercer numero: "))

# Ahora ingresamos a las condiciones compuestas
if(numero1 < 10 or numero2 < 10 or numero3 < 10):
    print("Alguno de los numeros es menor a diez")