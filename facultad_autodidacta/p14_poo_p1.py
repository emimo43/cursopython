# En esta clase veremos como crear clases en Python
'''
    Una clase es un contenedor -> consta de metodos y atributos
'''
# Para crear una clase usamos la palabra reservada class

class Persona: # Aqui comenzamos la creacion de la clase Persona
    
    def __init__(self, nombre, edad):
        # Para poder crear atributos se hace de la siguiente manera
        # Utilizamos self
        self.nombre = nombre
        self.edad = edad
        
# Aqui ya tenemos construido el constructor de la clase

# Ahora vamos a crear un metodo llamado saludar el cual nos mostrara algo por pantalla
    def saludar(self):
        print(f"Hola ¿Que tal? ", self.nombre)   
        
# Ahora creamos una funcion (metodo) la cual nos permitira mostrar la edad
    def mostrar_edad(self):
        print(f"La edad es: ", self.edad)        
        
# Ahora creamos un metodo que nos permitira hacer un ciclo if para ver la mayoria de edad de la Persona
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False           
        
# Ahora creamos otro metodo, el cual almacenara otros metodos
    def llamar_otro(self):
        self.saludar()
        self.mostrar_edad()
        print(self.es_mayor_de_edad())  # Se debe imprimir este metodo, como es booleano     
    
# Un objeto es la instancia de una clase
objeto_persona = Persona('Roldan', 34) # Creamos un objeto de la clase persona y le pasamos dos parametros

# Ahora usamos este objeto para poder llamos a la funcion saludar
objeto_persona.saludar()

# Ahora usamos este objeto para hacer la llamada al metodo que muestra la edad
objeto_persona.mostrar_edad()

# Ahora usamos este objeto para ver el resultado si la persona es mayor de edad o no
objeto_persona.es_mayor_de_edad()

# Pero para poder retornar este valor debo almacenar esta objeto en una variable
mejor_si_no = objeto_persona.es_mayor_de_edad()
# Ahora esta variable la imprimo
print(mejor_si_no)

# Ahora con el objeto llamamos al metodo llamar_otro()
objeto_persona.llamar_otro()
objeto_persona.llamar_otro()
objeto_persona.llamar_otro()
