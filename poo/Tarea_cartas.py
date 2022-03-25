from random import randint


class Carta:

    palo = ""

    valor = ""


    def __init__(self,palo,valor):

        self.palo = palo

        self.valor = valor

    def __str__(self):

        return self.valor + " de " + self.palo

    
    


class baraja:
    def __init__(self,cartas):


        self.cartas = cartas
    

    def robar_carta(self,cartas):
        deck.remove(deck[randint(0,len(deck)-1)])
        return deck[randint(0,len(deck)-1)]


    def shuffle(self):

        for i in range(len(self.cartas)-1,0,-1):

            j = randint(0,i)

            self.cartas[i],self.cartas[j] = self.cartas[j],self.cartas[i]

        return self.cartas



