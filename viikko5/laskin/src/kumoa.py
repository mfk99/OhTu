
class Kumoa:
    def __init__(self, sovelluslogiikka, luku):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self.sovelluslogiikka.aseta_arvo(self.sovelluslogiikka.viime_tulos)
