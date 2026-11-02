import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus_nollataan(self):
        varasto = Varasto(-10)
        self.assertAlmostEqual(varasto.tilavuus, 0.0)

    def test_nollataan_negatiivinen_alkusaldo(self):
        varasto = Varasto(10, -100)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_negatiivinen_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(3)
        self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(self.varasto.saldo, 3)

    def test_ei_liikaa_tavaraa_varastoon(self):
        varasto = Varasto(10, 30)

        self.assertAlmostEqual(varasto.saldo, 10)

    def test_negatiivinen_otto_palauttaa_nollan(self):
        maara = self.varasto.ota_varastosta(-7)

        self.assertAlmostEqual(maara, 0.0)

    def test_ei_voi_ottaa_enempaa_kuin_saldon(self):
        self.varasto.lisaa_varastoon(6)
        maara = self.varasto.ota_varastosta(100)

        self.assertAlmostEqual(maara, 6)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varasto_tayttyy_kun_enemman_kuin_tilaa(self):
        self.varasto.lisaa_varastoon(200)
        
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_stringitesti_palauttaa_mjonon(self):
        teksti = str(self.varasto)

        self.assertIn("saldo", teksti)
        self.assertIn("kakka", teksti)