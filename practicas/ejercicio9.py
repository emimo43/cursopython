"""Problema:
Ingresar el sueldo de una persona, si supera los 3000 dolares mostrar un mensaje en pantalla indicando que debe abonar impuestos"""

def sueldo():
    print("Favor ingresar el sueldo del trabajador: ")
    pago = int(input())
    if pago > 3000:
        print(f"El sueldo del trabajador es {pago} debe abonar impuestos")

sueldoTrabajador = sueldo() 
