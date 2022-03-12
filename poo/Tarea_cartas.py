class Carta:
    palo = ""
    valor = ""

    def __init__(self,palo,valor):
        self.palo = palo
        self.valor = valor

class baraja(Carta):
    def __init__(self,cartas)

    self.cartas = [
        "Ae","2e","3e","4e","5e","6e","7e","8e","9e","10e","Je","Qe","Re",
        "Ad","2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Rd",
        "Ac","2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Rc",
        "At","2t","3t","4t","5t","6t","7t","8t","9t","10t","Jt","Qt","Rt",    
        ]
    

    def robar(self):
