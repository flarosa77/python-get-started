# Leggiamo un file scorrendone il contenuto riga per riga (tramite il metodo readline())

file_divina = open('divina_commedia.txt', 'r')

while True:
    verso = file_divina.readline()
    if len(verso) == 0:
        break
    print(verso)

file_divina.close()
