from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.lista = []

    def tavaroita_korissa(self):
        return len(self.lista)

    def hinta(self):
        summa = 0
        for tuote in self.lista:
            summa += tuote.hinta()
        return summa

    def lisaa_tuote(self, lisattava: Tuote):
       self.lista.append(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.lista
