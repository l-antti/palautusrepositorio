from tuote import Tuote
from kirjanpito import kirjanpito as default_kirjanpito


class Varasto:
    def __init__(self, kirjanpito=default_kirjanpito):
        self._kirjanpito = kirjanpito
        self._saldot = {}
        self._alusta_tuotteet()


    def hae_tuote(self, id):
        for tuote in self._saldot:  # Tämä käy suoraan läpi sanakirjan avaimet
            if tuote.id == id:
                return tuote
        return None


    def saldo(self, id):
        tuote = self.hae_tuote(id)
        if tuote is None:  # Varmistetaan, että tuotetta löytyy
            raise ValueError(f"Tuotetta id {id} ei löytynyt varastosta.")
        return self._saldot[tuote]


    def ota_varastosta(self, tuote):
        saldo = self.saldo(tuote.id)
        if saldo <= 0:
            raise ValueError(f"Tuotetta {tuote} ei ole tarpeeksi varastossa.")
        self._saldot[tuote] = saldo - 1
        self._kirjanpito.lisaa_tapahtuma(f"otettiin varastosta {tuote}")


    def palauta_varastoon(self, tuote):
        saldo = self.saldo(tuote.id)
        self._saldot[tuote] = saldo + 1
        self._kirjanpito.lisaa_tapahtuma(f"palautettiin varastoon {tuote}")

    def _alusta_tuotteet(self):
        self._saldot[Tuote(1, "Koff Portteri", 3)] = 100
        self._saldot[Tuote(2, "Fink Bräu I", 1)] = 25
        self._saldot[Tuote(3, "Sierra Nevada Pale Ale", 5)] = 30
        self._saldot[Tuote(4, "Mikkeller not just another Wit", 7)] = 40
        self._saldot[Tuote(5, "Weihenstephaner Hefeweisse", 4)] = 15


varasto = Varasto()
