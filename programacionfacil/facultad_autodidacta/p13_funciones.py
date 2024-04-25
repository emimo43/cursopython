'''
    En esta clase veremos las funciones, esto es reutilizar codigo para poder volver a usarse
'''

# Vamos a crear una funcion, esta se hace usando la palabra reservada def
'''def saludar(): # En el parentesis se usan los parametros
    print("Saludar a los autodidactas")
    
# Ahora vamos a imprimir, esto se hace llamando a la funcion de la siguiente manera
saludar()    
# Ahora veremos como repetir esta llamada
saludar()
saludar()'''

# Ahora vermos como hacer una funcion con la funcion input
'''def saludar2 ():
    print("Favor salude a nuestros estudiantes ")
    nombre = input("Hola ¿Cual es tu nombre: ? ")
    print(f"Hola buenos dias, mi nombre es: {nombre}")
    
saludar2()    '''

# Ahora creamos una funcion que sume dos numeros
'''def sumar(numero1, numero2):
    resultado = numero1 + numero2 # Creamos una variable resultado la cual almacenara el resultado de la suma
    print(resultado)
    
sumar(6,90) # Aqui estamos llamando a la funcion
sumar(16,5)
sumar(100,90) '''

# Ahora haremos la funcion sumar, usando el ingreso de datos por teclado
'''def sumar2(): # Creamos la funcion
    # Ahora solicitamos los datos al Usuario
    numero1 = int(input("Favor ingrese el primer numero: "))
    numero2 = int(input("Favor ingrese el segundo numero: "))
    # Ahora creamos la variable resultado para obtener el valor requerido
    resultado = numero1 + numero2
    print(f"El resultado de la suma es: {resultado}")
    
# Ahora llamamos a la funcion
sumar2()           '''

# Ahora creamos una funcion resta, pero con la funcion return
'''def restar(numero1, numero2):
    return("La resta es: " + str(numero1 - numero2)) # Aqui resta los numeros y luego lo convierte a string

# Creamos una variable llamada resta, la cual contendra la funcion restar
resta = restar(8,4)
print(resta)'''

# Ahora haremos lo mismo pero con la funcion input
def restar2():
    numero3 = int(input("Favor ingresa el primer numero: "))
    numero4 = int(input("Favor ingrese el segundo numero: "))
    resultado = numero3 - numero4
    return(f"El valor de la resta es: {resultado}")
    

# Ahora creamos una variable llamado resta2 la cual contendra restar2
resta = restar2()
print(resta)
    