# Usiamo il ciclo for per stampare gli elementi di una "lista"
for i in [0,1,2,3]:
    print(i)

# Stampiamo una linea vuota sullo schermo
print()

# Usiamo il ciclo for per stampare gli elementi di un intervallo (definito tramite la funzione range())
# N.B.: l'estremo superiore non è incluso nell'intervallo
for i in range(0,5):
    print(i)

print()

# Usiamo il ciclo for per stampare gli elementi di un intervallo (definito tramite la funzione range())
# N.B.: in questo caso usiamo uno step ("2")
for i in range(0,5,2):
    print(i)

print()

# Usiamo il ciclo per contare alla rovescia con un step ("2")
for i in range(10, 0, -2):
    print(i)

print()



# Scorriamo gli elementi di una lista (di stringhe)
for c in ['zoff','gentile','cabrini','oriali','collovati','scirea','conti','tardelli','rossi','antonioni','graziani']:
    print(c)

print()



# Realizziamo uno snippet di codice che acquisisce due numeri interi e poi
# scorre gli interi (stampandoli a schermo) compresi tra i due estremi
a = input('Digita un numero intero positivo ')

a = int(a)

b = input('Digita un secondo numero intero positivo')

b = int(b)

for i in range(a,b):
    print(i)

print()


# Introduciamo il costrutto if-elif-else


a = input('Digita un numero intero positivo ')

a = int(a)

b = input('Digita un secondo numero intero positivo')

b = int(b)


if a > b:
    print('a è maggiore di b')
elif( a < b):
    print('b è maggiore di a')
else:
    print('a e b sono uguali')

print()



