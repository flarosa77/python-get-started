class Punto:
    """Una classe per rappresentare e operare con una coppia di coordinate x, y"""

    # aggiungiamo un metodo di classe
    @classmethod
    def origin(cls):
        """Metodo della classe che imposta i valori x=0, y=0"""
        return cls(0, 0)  # cls contiene tutte le informazioni sulla classe

    def __init__(self, x, y):
        """Inizializza le coordinate del punto"""
        self.x = x
        self.y = y





