"""Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero con el segundo y a este resultado se lo multiplica por el tercero"""

# Solicitamos los datos al usuario
numero1 = int(input("Favor ingresar el primer numero: "))
numero2 = int(input("Favor ingresar el segundo numero: "))
numero3 = int(input("Favor ingrese el tercer numero: "))

# Ahora generamos la condicion para realizar la operacion
if(numero1 == numero2 and numero1 == numero3 and numero2 == numero3):
    suma = numero1 + numero2
    multiplicacion = suma * numero3
    print(f"La suma del primer numero con el segundo es: {suma}")
    print(f"La multiplicacion del resultado de la suma con el tercer numero es: {multiplicacion}")