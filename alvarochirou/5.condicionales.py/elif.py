# elif cumple como el switch en otros lenguajes

letra = "u"

if letra.lower() =="a": # Con el metodo lower si ingresamos una mayuscula la convertira en minuscula
    print("Esta vocal es la A")
elif letra.lower() == "e":
    print("Esta vocal es la E")  
elif letra.lower() == "i":
    print("Esta vocal es la I")
elif letra.lower() == "o":
    print("Esta vocal es la O")
else:
    print("Esta vocal es la U")