from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.lista = {}

    def tavaroita_korissa(self):
        maara=0
        for key in self.lista:
            maara += self.lista.get(key)
		
        return maara

    def hinta(self):
        summa = 0
        for tuote in self.lista:
            maara = self.lista.get(tuote)
            summa += (tuote.hinta() * maara)
        return summa

    def lisaa_tuote(self, lisattava: Tuote):
        maara = self.lista.get(lisattava)
        if (maara == None):
            self.lista.update({lisattava: 1})
        else :
            self.lista.update({lisattava: maara + 1})

    def poista_tuote(self, poistettava: Tuote):
		
        maara = self.lista.get(poistettava)
        if (maara == 1):
            self.lista.pop(poistettava)
        else: self.lista.update({poistettava: maara-1})

    def tyhjenna(self):
        self.lista={}

    def ostokset(self):
        return list(self.lista.keys())

