'''
Problema:
    Se cargan por teclado tres numeros distintos. Mostrar por pantalla el mayor de ellos

'''
# Solicitamos los datos del Usuario
numero1 = int(input("Favor ingresar el primer numero: "))
numero2 = int(input("Favor ingresar el seggundo numero: "))
numero3 = int(input("Favor ingresar el tercer numero: "))

# Ingresamos al ciclo if para validar los resultados

if numero1 > numero2:
    if numero1 > numero3:
        print(f"El numero 1 -> {numero1} es el mayor")
else:
    if numero2 > numero1:
        if numero2 > numero3:
            print(f"El numero 2 -> {numero2} es el mayor")
            
    if numero3 > numero2:
        if numero3 > numero1:
            print(f"El numero 3 ->  {numero3} es el numero mayor")        
    
         
                
print("")
print("Fin del Programa")                            