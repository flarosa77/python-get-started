class Punto:
    """Una classe per rappresentare e operare con una coppia di coordinate x, y"""

    @classmethod
    def origin(cls):
        """Metodo della classe che imposta i valori x=0, y=0"""
        return cls(0, 0)  # cls contiene tutte le informazioni sulla classe

    def __init__(self, x, y):
        """Inizializza le coordinate del punto"""
        self.x = x
        self.y = y

    # aggiungiamo un metodo statico
    @staticmethod
    def coordinata_valida(x):  # NON c'è self: non so nulla dell'istanza
        """Controllo se la coordinata è entro il limite 100"""
        return x < 100

    # aggiungiamo un metodo speciale
    """Special Methods"""
    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"







