from random import randint

class Carta:
    palo = ""
    valor = ""

    def __init__(self,palo,valor):
        self.palo = palo
        self.valor = valor

class baraja:
    def __init__(self,cartas):

        self.cartas = cartas
    

    def shuffle(cartas):

        shuffle_cards = cartas.copy()

        x = len(shuffle_cards)
        for i in range(x-1,0,-1):
            j = randint(0,i)
            shuffle_cards[i],shuffle_cards[j] = shuffle_cards[j], shuffle_cards[i]
        return shuffle_cards

