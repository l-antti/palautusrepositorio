from tkinter import ttk, constants, StringVar

class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root
        self._edellinen_komento = None

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento("summa")
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento("erotus")
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento("nollaus")
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=self._kumoa
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _suorita_komento(self, komento):
        if komento == "summa":
            self._edellinen_komento = Summa(self._sovelluslogiikka)
        elif komento == "erotus":
            self._edellinen_komento = Erotus(self._sovelluslogiikka)
        elif komento == "nollaus":
            self._edellinen_komento = Nollaus(self._sovelluslogiikka)

        self._edellinen_komento.suorita(self._lue_syote)
        self._paivita_napit()

    def _kumoa(self):
        if self._edellinen_komento:
            self._edellinen_komento.kumoa()
            self._paivita_napit()

    def _paivita_napit(self):
        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        if self._edellinen_komento:
            self._kumoa_painike["state"] = constants.NORMAL
        else:
            self._kumoa_painike["state"] = constants.DISABLED

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())

    def _lue_syote(self):
        return self._syote_kentta.get()
    
class Komento:
    def __init__(self, sovelluslogiikka):
        self._sovelluslogiikka = sovelluslogiikka
        self._edellinen_arvo = sovelluslogiikka.arvo()

    def suorita(self, lue_syote):
        syote = lue_syote()
        try:
            arvo = int(syote) if syote else 0
        except ValueError:
            arvo = 0

        self.suorita_toiminto(arvo)

    def suorita_toiminto(self, arvo):
        raise NotImplementedError("Tämä metodi tulee toteuttaa alaluokassa!")

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_arvo)

class Summa(Komento):
    def suorita_toiminto(self, arvo):
        self._sovelluslogiikka.plus(arvo)

class Erotus(Komento):
    def suorita_toiminto(self, arvo):
        self._sovelluslogiikka.miinus(arvo)

class Nollaus(Komento):
    def suorita_toiminto(self, arvo):
        self._sovelluslogiikka.nollaa()

