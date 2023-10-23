# Leggiamo un file e copiamo il suo contenuto in una classe "list"
# tramite il metodo readlines()


file_divina = open('divina_commedia.txt', 'r')
contenuto = file_divina.readlines()
file_divina.close()
print(contenuto)
print(type(contenuto))
