from OOP5 import Punto


# Un esempio di ereditarietà in Python
class PuntoMassa(Punto):
    """Classe per rappresentare un punto con massa"""
    g = 9.81

    # ridefiniamo il costruttore
    def __init__(self, x=0, y=0, m=0):
        """Sovrascrive l'__init__ di Punto per tenere conto della massa"""
        super().__init__(x, y)  # Per le coordinate, uso l'__init__ di 'Punto'
        # NOTA: uso SUPER
        self.m = m  # Aggiungo il nuovo attributo: massa

    # aggiungiamo un metodo nella classe figlia
    def peso(self):
        """Restituisce il peso dell'oggetto"""
        return self.m*self.g


