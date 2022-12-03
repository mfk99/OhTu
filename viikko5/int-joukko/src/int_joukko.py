KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = [self.kapasiteetti]
        self.alkioiden_lkm = 0

    def kuuluu(self, kohde_alkio):

        for alkio in self.ljono:
            if kohde_alkio == alkio: return True
        
        return False

    def lisaa(self, kohde_alkio):

        if self.kuuluu(kohde_alkio): 
            return False
        
        self.ljono[self.alkioiden_lkm] = kohde_alkio
        self.alkioiden_lkm = self.alkioiden_lkm + 1

        if (self.alkioiden_lkm == len(self.ljono)):
            self.kasvata()
            
        return True

    def kasvata(self):
        aputaulukko = self.ljono
        self.kopioi_taulukko(self.ljono, aputaulukko)
        self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_taulukko(aputaulukko, self.ljono)

    def poista(self, kohde_alkio):

        if (not self.kuuluu(kohde_alkio)):
            return False

        kohde_indeksi = -1
        apu = 0

        for i in range(0, self.alkioiden_lkm):
            if kohde_alkio == self.ljono[i]:
                kohde_indeksi = i 
                self.ljono[kohde_indeksi] = 0
                break

        for j in range(kohde_indeksi, self.alkioiden_lkm - 1):
            apu = self.ljono[j]
            self.ljono[j] = self.ljono[j + 1]
            self.ljono[j + 1] = apu

        self.alkioiden_lkm = self.alkioiden_lkm - 1
        return True

    def kopioi_taulukko(self, kopioitava, kopio):
        for i in range(0, len(kopioitava)):
            kopio[i] = kopioitava[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for alkio in a_taulu:
            yhdiste.lisaa(alkio)

        for alkio in b_taulu:
            yhdiste.lisaa(alkio)

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for alkio_a in a_taulu:
            for alkio_b in b_taulu:
                if alkio_a == alkio_b:
                    leikkaus.lisaa(alkio_a)

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for alkio in a_taulu:
            erotus.lisaa(alkio)

        for alkio in b_taulu:
            erotus.poista(alkio)

        return erotus

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
