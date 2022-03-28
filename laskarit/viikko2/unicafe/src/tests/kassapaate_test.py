import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestMaksupaate(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)
        self.kassapaate=Kassapaate()
    
    def test_uusi_kassapaate_oikein(self):
            self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
            self.assertEqual(self.kassapaate.edulliset, 0)
            self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_toimii_kateisella(self):
            self.kassapaate.syo_edullisesti_kateisella(240)
            self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
            self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukkaasti_toimii_kateisella(self):
            self.kassapaate.syo_maukkaasti_kateisella(400)
            self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
            self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_syo_edullisesti_toimii_kortilla(self):
            self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
            self.assertEqual(str(self.maksukortti), "saldo: 7.6")
            self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukkaasti_toimii_kortilla(self):
            self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
            self.assertEqual(str(self.maksukortti), "saldo: 6.0")
            self.assertEqual(self.kassapaate.maukkaat, 1)
            return True
   
    def test_lataa_rahaa_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    def test_syo_edullisesti_liian_vahan_rahaa_toimii_kateisella(self):
            self.kassapaate.syo_edullisesti_kateisella(200)
            self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
            self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_liian_vahan_rahaa_toimii_kateisella(self):
            self.kassapaate.syo_maukkaasti_kateisella(300)
            self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
            self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_syo_edullisesti_liian_vahan_saldoa_toimii_kortilla(self):
            self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
            self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
            self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
            self.assertEqual(str(self.maksukortti), "saldo: 2.0")
            self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_liian_vahan_saldoa_toimii_kortilla(self):
            self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
            self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
            self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
            self.assertEqual(str(self.maksukortti), "saldo: 2.0")
            self.assertEqual(self.kassapaate.maukkaat, 2)
   
    def test_lataa_rahaa_negatiivinen_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

