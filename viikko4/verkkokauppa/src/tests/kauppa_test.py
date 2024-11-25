import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())
        self.varasto_mock = Mock()

        self.viitegeneraattori_mock.uusi.return_value = 42

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 5

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                return Tuote(2, "leipä", 3)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)

        self.kauppa.tilimaksu("pekka", "12345")


        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

    def test_ostoksen_paatyttya_kaksi_erilaista_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)

        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 8)

    def test_ostoksen_paatyttya_kaksi_samaa_tuotetta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)

        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)

    def test_ostoksen_paatyttya_varastossa_on_tuote_ja_toista_ei(self):
        self.kauppa.aloita_asiointi()
        
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10  
            elif tuote_id == 2:
                return 0  

    
        self.varasto_mock.saldo.side_effect = varasto_saldo


        self.kauppa.lisaa_koriin(1) 
        self.kauppa.lisaa_koriin(2) 

        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)


    def test_aloita_asiointi_nollaa_edellisen_ostoksen_tiedot(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.assertEqual(self.kauppa._ostoskori.hinta(), 5)

        self.kauppa.aloita_asiointi() 
        self.kauppa.lisaa_koriin(2)
        self.assertEqual(self.kauppa._ostoskori.hinta(), 3)


    def test_uusi_viitenumero_jokaiselle_maksulle(self):
        self.viitegeneraattori_mock.uusi.side_effect = [100, 200, 300]

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("1111", "1234-12345")

        self.pankki_mock.tilisiirto.assert_called_with("1111", 100, "1234-12345", "33333-44455", 5)
        
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("1234", "5432-12345")

        self.pankki_mock.tilisiirto.assert_called_with("1234", 200, "5432-12345", "33333-44455", 3)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("4444", "6789-12345")

        self.pankki_mock.tilisiirto.assert_called_with("4444", 300, "6789-12345", "33333-44455", 3)

    def test_poista_korista_yksi_tuote(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1) 
        
        self.kauppa.poista_korista(1)
        
        self.assertEqual(self.kauppa._ostoskori.hinta(), 0)
        self.assertEqual(len(self.kauppa._ostoskori.sisalto()), 0)