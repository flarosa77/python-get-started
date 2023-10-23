# Operazioni sulle stringhe in Python

# Inizializziamo una stringa
string = 'Hello world!'

# Accediamo ad un carattere della stringa
print(string[4])
print()

# Scorriamo i caratteri della stringa usando un ciclo for
for s in string:
    print(s)

# Usiamo i metodi della classe "str"

# Rendiamo maiuscole tutte le lettere della stringa
print(string.upper())

# Invertiamo tutte le lettere della stringa (maiuscola-minuscola e minuscola-maiuscola)
print(string.swapcase())
print()

# Concatenazione di stringhe

# Inizializziamo le variabili che useremo per fare degli esempi
nome = 'Giangeppo'
anni = 42
altezza = 1.75

# First Method
out = 'Mi chiamo ' + nome + ', ho ' + str(anni) + ' anni e sono alto ' + str(altezza) + '. Tra 145 anni avrò ' + str(
    anni + 145) + ' anni'
print(out)

# Second Method
print('Mi chiamo', nome, ', ho ', anni, ' anni e sono alto ', altezza, '. Tra 145 anni avrò ', anni + 145, ' anni')

# Third Method
out = "Mi chiamo %s, ho %i anni e sono alto %.2f. Tra 145 anni avrò %d anni" % (nome, anni, altezza, anni + 145)
print(out)

# Fourth Method
out = "Mi chiamo {}, ho {} anni e sono alto {}. Tra 145 anni avrò {} anni".format(nome, anni, altezza, anni + 145)
print(out)

# Fifth Method
out_1 = "Il signor {name} ha {age} anni".format(name=nome, age=anni)
print(out_1)
print()

out_2 = "Il signore di {age} anni è {name}".format(name=nome, age=anni)
print(out_2)
print()

# Last Method (f-strings)
out = f"Mi chiamo {nome}, ho {anni} anni e sono alto {altezza}. Tra 145 anni avrò {anni + 145} anni"
print(out)
print()
