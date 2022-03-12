


class Vehiculo: 
    marca = ""
    color = ""
    modelo = ""
    year = ""
    is_verif = ""
    dias_servicio = ""
    encendido = "" 
    
    def __init__ (self, marca, color, modelo, year, is_verif, dias_servicio):
        self.marca = marca #Se llama igual la variable que se esta definiendo para que a la hora de imprimir el objeto, se imprima el valor de la variable.
        self.color = color
        self.modelo = modelo
        self.year = year
        self.is_verif = is_verif
        self.dias_servicio = dias_servicio
        self.encendido = False
    
    
    def encender_autou(self): #Los metodos propios de la clase deben ir definidos dentro de la clase, para posteriormente ser llamados. 
        self.encendido = True
    def apagar_autou(self):
        self.encendido = False

        


class Moto(Vehiculo):
    tipo = ""
    cilindraje = ""

    def __init__ (self, marca, color, modelo, year, is_verif, dias_servicio, tipo, cilindraje):
        super().__init__(marca, color, modelo, year, is_verif, dias_servicio)
        self.tipo = tipo
        self.cilindraje = cilindraje
