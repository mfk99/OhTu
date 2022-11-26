from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.maara=0
        self.summa=0
        pass
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return self.maara

    def hinta(self):
        return self.summa

    def lisaa_tuote(self, lisattava: Tuote):
       self.maara += 1 
       self.summa += lisattava.hinta()

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
