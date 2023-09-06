# El ciclo if solo se cumple si la condicion es verdadera
edad = int(input("¿Cuantos años tienes? "))

if edad == 100:
    print("Tienes un siglo de vida")
elif edad >= 18:
    print("Eres mayor de edad!")    
else:
    print("Eres menor de edad")    