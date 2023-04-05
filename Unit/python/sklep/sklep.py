class Produkt:
    __cena = 0
    __nazwa = None

    def __init__(self, cena, nazwa):
        self.__cena = cena
        self.__nazwa = nazwa

    def cena_produktu(self):
        return self.__cena

    def __str__(self):
        return f'{self.__nazwa}:{self.__cena}'


class Koszyk:
    __produkty = []

    def wrzuc(self, produkt):
        self.__produkty.append(produkt)

    def podlicz(self):
        kupione = 0
        for produkt in self.__produkty:
            kupione += produkt.cena_produktu()
        return kupione

    def wez_produkty(self):
        return self.__produkty


def do_kasy(pieniadze:int, koszyk:Koszyk)-> int:
    if pieniadze < koszyk.podlicz():
        return 0

    return pieniadze-koszyk.podlicz()