class FirstClass:
    """Docstring per descrivere l'oggetto"""
    attributo = 5  # attributo (dati) dell'oggetto

    def metodo_aggiungi(self):  # istruzioni (metodo) per interagire (self)
        self.attributo += 1  # operazione su attributi dell'oggetto (self)


# aggiungiamo un metodo alla classe "Punto"
class Punto:
    """Una classe per rappresentare e operare con una coppia di coordinate x, y come punto su un piano"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distanza_da_origine(self):
        """Calcola la distanza dall'origine"""
        return (self.x ** 2 + self.y ** 2) ** 0.5




