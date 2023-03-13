class Lampka:
    def __init__(self):
        self.__czy_wlaczona=False #wyłączona
        
    def pstryk(self):
        if not self.__czy_wlaczona:   # jeśli jest wyłaczona
            self.__czy_wlaczona=True  # włączamy
        else:
            self.__czy_wlaczona=False # lub wyłaczamy
        return self.__czy_wlaczona
