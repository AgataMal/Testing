import unittest
import sklep

class UnitTests(unittest.TestCase):

    def test_sklep(self):
        pomidor=sklep.Produkt(20, "pomidor")
        cebula=sklep.Produkt(2, "cebula")
        koszyk=sklep.Koszyk()
        koszyk.wrzuc(cebula)
        koszyk.wrzuc(pomidor)
        self.assertEqual(sklep.do_kasy(50,koszyk),28)
        self.assertEqual(sklep.do_kasy(10,koszyk),0)


    def test_pusty_koszyk(self):
        koszyk=sklep.Koszyk()
        self.assertEqual(sklep.do_kasy(10,koszyk),10)
