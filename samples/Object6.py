from OOP5 import Punto

# Usiamo un metodo statico
'''Questi metodi non necessitano di una istanza della classe per essere chiamati'''
if Punto.coordinata_valida(200):
    print("Coordinata valida")
else:
    print("Coordinata non valida")

p = Punto(30, 50)

print(p.__str__())











