KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = self._validoi_kapasiteetti(kapasiteetti)
        self.kasvatuskoko = self._validoi_kapasiteetti(kasvatuskoko)
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def _validoi_kapasiteetti(self, koko):
        if not isinstance(koko, int) or koko < 0:
            raise Exception("Kapasiteetti ja kasvatuskoko tulee olla positiivisia lukuja.")
        return koko

    def _luo_lista(self, koko):
        return [0] * koko

    def kuuluu(self, n):
        return n in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, n):
        if not self.kuuluu(n):
            if self.alkioiden_lkm == len(self.ljono):
                self._kasvata_lista()


            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            return True
        return False

    def _kasvata_lista(self):
        uusi_lista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        for i in range(self.alkioiden_lkm):
            uusi_lista[i] = self.ljono[i]
        self.ljono = uusi_lista

    def poista(self, n):
        if n in self.ljono[:self.alkioiden_lkm]:
            self.ljono.remove(n)
            self.alkioiden_lkm -= 1
            return True
        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        for alkio in a.to_int_list() + b.to_int_list():
            x.lisaa(alkio)
        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for alkio in a_taulu:
            if alkio in b_taulu:
                y.lisaa(alkio)
        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        for alkio in a.to_int_list():
            z.lisaa(alkio)
        for alkio in b.to_int_list():
            z.poista(alkio)
        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        return "{" + ", ".join(map(str, self.ljono[:self.alkioiden_lkm])) + "}"
