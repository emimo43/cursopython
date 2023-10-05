"""Se cargan por teclado tres numeros distintos. Mostrar por pantalla el mayor de ellos"""

# Solicitamos los datos al Usuario
num1 = int(input("Favor ingresar el primer numero: "))
num2 = int(input("Favor ingresar el segundo numero: "))
num3 = int(input("Favor ingresar el tercer numero: "))

# Ahora veremos las condiciones
if(num1 > num2 and num1 > num3):
    print(f"{num1} es el mayor")
else:
    if(num2 > num1 and num2 > num3):
        print(f"{num2} es el mayor")
    else:
        print(f"{num3} es el mayor")    
    