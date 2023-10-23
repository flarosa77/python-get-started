# Leggiamo un file e copiamo il suo contenuto in una classe "str"
# tramite il metodo read()

file_divina = open('divina_commedia.txt', 'r')
contenuto = file_divina.read()
file_divina.close()
print(contenuto)
print(type(contenuto))
