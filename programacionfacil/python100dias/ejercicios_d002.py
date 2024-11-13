'''
    Ejercicio dia 2 del challenge de Python
'''
# 1.- ¿Cuales de estos strings son correctos?
#print("Hoy es un gran dia para progranar")
#print('¿Que día es hoy?')

# 3.- Imprime en la consola el numero de caracteres que tiene la palabra <automaticamente>. Lo puedes hacer con variable o directamente con un print()

#frase = "automáticamente"
#print(len(frase)) # Con el metodo len() vemos cuantos caracteres tiene la variable frase

# 4.- ¿Sabrias mostrar en la consola solo el caracter de la <á> con acento de <automáticamente>? Lo debes hacer mediante las posiciones de string
#print(frase[5]) # Corresponde al caracter á

# 5.- Realiza la operacion de 10 elevaro a 5 con el uso del operador exponente
#potencia = 10 ** 5
#print(potencia)
#print(type(potencia))

# 6.- Ahora ¿Como harías es operacion sin el operador exponente
#multiplicacion = 10 * 10 * 10 * 10 * 10
#print(multiplicacion)
#print(type(multiplicacion))

# 8.- Muestra en consola el tipo de dato que contiene esta variable <numero_1 = 675.87>
#numero_1 = 675.87
#print(type(numero_1))

# 9.- Muestra la cantidad de digitos que tiene este numero (768763843) utilizando la funcion len()
#print(len(768763843)) # No se puede debido a que esta funcion solo es con str

# 10.- Haz ue estos datos float, se conviertan en integer mediante la conversion de tipos:
#numero_1 = "14.527"
#numero_2 = "560.92"
# No se pueden convertir por que son str

# 11.- Redondea estos numeros con la cantidad de decimales indicada en los comentarios e imprimelos en consola
'''
numero_1 = 10.897654876534 # 3 decimales
numero_2 = 7674.7886 # 2 decimales
numero_3 = 68754.78 # 1 decimal

print(round(numero_1,3))
print(round(numero_2,2))
print(round(numero_3,1))
'''
# 13.- Asigna con los operadores de asignacion de incremento o decremento los siguientes valores indicados en los comentarios
'''
numero_1 = 10 # +60
numero_2 = 24 # -100
numero_3 = 65.67 # +4.33

numero_1 += 60 # Incrementamos en 60 el valor de la variable
nmero_2 -= 100 # Decrementamos en 100 el valor de la variable
numero_3 += 4.33 # Incrementamos el valor en 4.33

print(numero_1) # Resultado es 70
print(numero_2) # Resultado es -76
print(numero_3) # Resultado es 70.0
'''
'''
# 14.- Mediante la tecnica de formateo de strings (recuerda el prefijo f) muestra literalmente todos estos valores en una frase print() sin utilizar la concatenacion.
# La frase es esta:
<El valor 769.97 es bastante mas grande que 4. ¿Am I a string? The answer is True.>
Quiero que intentes imprimirla exactamente igual
'''
'''
numero_1 = 4
numero_2 = 769.97
texto = "am I a string"
desicion = True

print(f"El valor {numero_2} es bastante mas grande que {numero_1}. ¿{texto}? The answer is {desicion}")
'''

'''
    15.- Llegamos al proyecto. Esta vez a construir una calculadora sencillita de exponentes. Esta calculadora, deberia pedirle al usuario los numeros que quiere. Aqui tienes un ejemplo de la salida en consola, para que te hagas una idea de como hacerlo.
    
    Resultado en la consola
    
    -Calculadora de exponentes
    Introduzca el primer numero
    10
    Introduzca el segundo numero
    4
    El resultado de 10 elevado a 4 es 10000
    
'''
# Solicitamos los datos al usuario
numero = int(input("Favor introduzca el numero: "))
exponente = int(input("Favor introduzca el exponente: "))

exponenciacion = numero ** exponente

print(f"El resultado de {numero} elevado a {exponente} es {exponenciacion}")
