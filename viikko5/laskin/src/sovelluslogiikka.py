class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.viime_tulos = 0
        self.tulos = tulos

    def aseta_arvo(self, arvo):
        self.viime_tulos = self.tulos
        self.tulos = arvo
