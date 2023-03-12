class Lampka:
    def __init__(self):
        self.czy_wlaczona=False #wyłączona
    def pstryk(self):
        if not self.czy_wlaczona:   # jeśli jest wyłaczona
            self.czy_wlaczona=True  # włączamy
        else:
            self.czy_wlaczona=False # lub wyłaczamy