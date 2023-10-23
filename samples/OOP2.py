# E' possibile definire due classi nello stesso file .py
class FirstClass:
    """Docstring per descrivere l'oggetto"""
    attributo = 5  # attributo (dati) dell'oggetto

    def metodo_aggiungi(self):  # istruzioni (metodo) per interagire (self)
        self.attributo += 1  # operazione su attributi dell'oggetto (self)


# Introduciamo il concetto di costruttore
class Punto:
    """Una classe per rappresentare e operare con una coppia di coordinate x, y come punto su un piano"""

    def __init__(self):
        self.x = 0
        self.y = 0
