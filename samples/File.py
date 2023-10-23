# Creiamo un file scrivendo al suo interno il contenuto di una stringa

file_divina = open('divina_commedia.txt', 'w')  # Apro un file in scrittura

divina = '''Nel mezzo del cammin di nostra vita mi ritrovai per una selva oscura,
ché la diritta via era smarrita.
Ahi quanto a dir qual era è cosa dura,
esta selva selvaggia e aspra e forte,
che nel pensier rinova la paura!'''

for riga in divina.split('\n'):  # Ciclo sulle righe che compongono la stringa multilinea
    file_divina.write(f'{riga}\n')  # Scrivo la riga nel file (ricordandomi di andare a capo con \n)

file_divina.close()  # Chiudo il file
