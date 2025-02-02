from kps import KiviPaperiSakset


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus in ["a", "b", "c"]:
            peli = KiviPaperiSakset.luo_peli(vastaus)
            print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
            peli.pelaa()
        else:
            print("Peli lopetetaan.")
            break


if __name__ == "__main__":
    main()
