class Ostoskori:
    def __init__(self):
        self._tuotteet = []
    
    def lisaa(self, tuote):
        self._tuotteet.append(tuote)
    
    def poista(self, tuote):
        self._tuotteet = list(
            filter(lambda t: t.id != tuote.id, self._tuotteet)
        )

    def hinta(self):
        hinnat = list(map(lambda t: t.hinta, self._tuotteet))
        return sum(hinnat)
    
    def sisalto(self):
        return self._tuotteet 
