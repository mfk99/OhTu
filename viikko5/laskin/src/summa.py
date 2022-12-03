
class Summa:
    def __init__(self, sovelluslogiikka, luku):
        self.sovelluslogiikka = sovelluslogiikka
        self.luku = luku

    def suorita(self):
        tulos = int(self.luku()) + self.sovelluslogiikka.tulos
        self.sovelluslogiikka.aseta_arvo(tulos)
