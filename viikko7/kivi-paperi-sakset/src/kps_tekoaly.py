from kps import KiviPaperiSakset
from tekoaly import Tekoaly

class KPSTekoaly(KiviPaperiSakset):
    def _toisen_siirto(self):
        tekoaly = Tekoaly()
        return tekoaly.anna_siirto()