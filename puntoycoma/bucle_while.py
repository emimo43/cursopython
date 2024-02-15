'''
while -> es una estructura que nos permite repetir un bloque de codigo mientras una condicion es verdadera
'''

edad = int(input("Ingrese su edad: "))

while edad < 0:
    print("La edad se cargo incorrectamente")
    edad = int(input("Ingrese su edad nuevamente: "))
    
print(f"La edad de la persona es: {edad}")    
    
    
    

'''for i in range(5):
    edad = int(input("Ingrese su edad: "))
    
    if edad < 0:
        print("La edad se cargo incorrectamente")
        
    print(f"La persona n°, {i} lista")    
    
    NO ESTA BIEN ESTA LOGICA
    
'''    

for i in range(5):
    edad = int(input("Ingrese su edad: "))
    
    while edad < 0:
        print("La edad se cargo incorrectamente")
        edad = int(input("Ingrese su edad nuevamente: "))
        
    print("Persona n°", i + 1, "lista")
    

    
    