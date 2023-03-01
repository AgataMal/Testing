class Produkt:
    cena = 0
    nazwa = None

    def __init__(self, cena, nazwa):
        self.cena = cena
        self.nazwa = nazwa

    def cena_produktu(self):
        return self.cena


class Koszyk:
    produkty = []

    def wrzuc(self, produkt):
        self.produkty.append(produkt)

    def podlicz(self):
        kupione = 0
        for produkt in self.produkty:
            kupione += produkt.cena_produktu()
        return kupione

    def wez_produkty(self):
        return self.produkty


def do_kasy(pieniadze:int, koszyk:Koszyk)-> int:
    return pieniadze-koszyk.podlicz()