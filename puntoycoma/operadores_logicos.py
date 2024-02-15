# En esta clase veremos los operadores logicos en python

# if -> si pero condicional
# > < -> mayor que - menor que
# == -> igual que

# Y -> Conjuncion -> 2 condiciones tienen que ser verdaderas para que la condicion se cumpla

edad = 48
carnet = True
'''La edad tiene que ser myor a 18 años y tiene que tener la licencia de conducir'''

if edad > 18 and carnet == True:
    print("Puede manejar")
else:
    print("No puede manejar")    
    
    
''' o -> disyuncion -> por lo menos una de las dos condiciones tienen que ser verdaderas para que la condicion se cumpla'''  

usuario_premium = False
saldo_suficiente = True

if usuario_premium or saldo_suficiente:
    print("Puede realizar la compra")
else:
    print("No puede realizar la compra")      
    
    
''' not -> negacion -> invertir la condicion que nos devuelva como resultado final'''    

usuario_bloqueado = True

if not usuario_bloqueado:
    print("Inicio de sesion exitoso")
else:
    print("Disculpa Master, no puedes entrar. NO te quieren")    