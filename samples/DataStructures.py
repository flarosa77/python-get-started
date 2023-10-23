"""
In questo corso, vedremo le quattro principali Data Structure che Python mette a disposizione:
La lista: list
La tupla: tuple
Il set: set
Il dizionario: dict
"""

# Liste

'''La lista è una collezione ordinata di valori. I valori che compongono la lista vengono chiamati elementi (item) della lista.
Un oggetto di tipo list si definisce racchiudendo gli elementi che lo compongono tra parentesi quadre [ ] , separati da ",".
Gli elementi di una lista possono essere di qualunque tipo.'''

# Inizializziamo un oggetto di tipo List
list = ['orange', 'apple', 'banana', 'pear']

# Accediamo al terzo ([2]) elemento della lista
elem = list[2]

print(elem)
print()

# Copiamo nella variabile subList una porzione di lista
# e dopo ne stampiamo il contenuto
sublist = list[1:3]

for c in sublist:
    print(c)

# Modifichiamo, assegnando il valore 'strawberry', il primo elemento della lista
list[0] = 'strawberry'

print()

# Una lista può contenere elementi di tipo di verso
# Un elemento della lista può essere a sua volta una lista
nums = [1, 2, [10, 11], 'ciao']

for value in nums:
    print(value)

# Usiamo alcuni dei metodi della classe "List"

# Ordiniamo la lista e stampiamo il suo contenuto
list.sort()
print(list)
print()

# Determiniamo e stampiamo a schermo la lunghezza della lista
len = len(list)
print(len)
print()

# Duplichiamo il contenuto della lista
list = list * 2
print(list)
print()

# Usiamo il metodo count per determinare quante volte la stringa "banana"
# si ripete nella lista
times = list.count('banana')
print('Banana appears ' + str(times) + ' times')
print()

# Troviamo la posizione di "strawberry" all'interno di list
index = list.index('strawberry')
print(index)
print()

# Cancelliamo l'elemento di indice "2"
print(list)
print()
del list[2]
print(list)
print()

# Tuple

'''
Le tuple sono utili per raggruppare insieme informazioni in qualche modo correlate tra loro.
Un oggetto di tipo tuple è una sequenza di valori separati da virgola , (comma-separated). 
Sebbene non sia necessario, per convenzione si racchiude la sequenza tra parentesi tonde ( ) .
Il tipo è immutabile, quindi, come per str , non possiamo modificare un'istanza di tipo  
una volta che è stata creata, a differenza di quanto facevamo con le list.
Possiamo quindi accedere ai singoli elementi della tupla, con il solito operatore [].
'''

# Creiamo una tupla
ibra = ("Zlatan", "Ibrahimovic", 11, "Milan", 1.95, 95, "Attaccante")

# Stampiamo il contenuto della tupla usando la funzione print()
print(ibra)
print()

# Leggiamo un elemento della tupla "ibra"
elem = ibra[2]
print(elem)
print()

# La modifica di un item non è possibile
# Syntax error!
# ibra[2] = 10

'''Una funzionalità molto comoda che Python mette a disposizione è l'assegnazione di variabili
 tramite tuple, o tuple assignment.'''

(nome, cognome, numero, squadra, altezza, peso, ruolo) = ibra

print(nome + " " + cognome)
# print(nome, cognome, numero)
print()

'''Potremmo scrivere una funzione che restituisca due valori: la somma e la differenza di due numeri. 
La tupla ci consente di raggruppare insieme quanti più valori vogliamo e di restituire un solo oggetto
 di tipo tuple tramite return :'''


def moreReturn(a, b):
    c = a + b
    d = a - b
    return (c, d)


output = moreReturn(10, 5)

print(output)
print()

'''Un set è una collezione di elementi non ordinata. A differenza di liste e tuple, ogni
elemento del set deve essere unico e non modificabile. Tuttavia l'oggetto di tipo set è modificabile.
Un oggetto di tipo set si definisce racchiudendo gli elementi che lo compongono tra parentesi graffe { } , separati da , .
Un altro modo per costruire un set è quello di usare la funzione built-in set() .'''

# Inizializziamo un set
setNumbers = {4, 8, 2, 23}
print(setNumbers)
print()

# Aggiungiamo un elemento nel set
setNumbers.add(57)
print(setNumbers)
print()

# Rimuoviamo un elemento dal set (in base al suo valore)
setNumbers.remove(8)
print(setNumbers)
print()

# Creiamo un secondo set
setSecond = {90, 100, 200}

# Creiamo un terzo set unendo i primi due
newSetNumbers = setNumbers.union(setSecond)
print(newSetNumbers)
print()

# Con un ciclo for scorriamo gli elementi di un set
for num in newSetNumbers:
    print(num)

# Aggiorniamo il set (aggiungengo degli elementi, se non sono già presenti!)
newSetNumbers.update([1, 2, 3])
print(newSetNumbers)
print()

# Rimuoviamo degli elementi dal set
newSetNumbers.discard(2)
newSetNumbers.remove(3)

print(newSetNumbers)
print()

'''Dizionari
Finora, escludendo i set, abbiamo sempre parlato di sequenze: tipi composti che permettono di accedere ai singoli elementi che li compongono tramite indici interi.
I dizionari rappresentano un tipo composto (compund data type) diverso. Il tipo dict rappresenta quello che viene definito built-in mapping type di Python.
Un dizionario mappa una serie di chiavi (keys) ai relativi valori (values). La chiave può essere di qualunque tipo non modificabile, solitamente si usa il tipo str , 
mentre il valore può assumere qualunque tipo. Un oggetto di tipo dict si definisce racchiudendo gli elementi che lo compongono tra parentesi graffe { } , separati da , . 
Ogni elemento che compone il dizionario è una coppia chiave-valore, definita dalla sintassi chiave:valore :'''

# Inizializziamo un Dictionary
inventory = {"banane": 7, "lamponi": 11}

# Stampiamo un elemento del Dictionary
print(inventory['banane'])
print()

'''I dizionari sono una Data Structure modificabile.
Per assegnare una nuova coppia chiave-valore a un dizionario, usiamo la seguente sintassi:'''

inventory['mele'] = 5
inventory['lamponi'] = 10

print(inventory)
print()

# Stampiamo a schermo le chiavi di un dictionary
print(inventory.keys())
print()

# Scorriamo tramite un ciclo for le chiavi di un dictionary
for key in inventory.keys():
    testo = "Numero di " + key + " nell'inventario:"
    valore = inventory[key]
    print(testo, valore)

# Stampiamo a schermo i valori di un dictionary
print(inventory.values())

# Stampiamo a schermo chiavi e valori di un dictionary
print(inventory.items())

# Leggiamo un elemento del dictionary usando la chiave "banane" e stampiamo a schermo il valore
numBanane = inventory.get('banane')
print(numBanane)

'''
List comprehension, set comprehension e dict comprehension
Python fornisce una sintassi compatta per generare liste, set e dizionari a partire da sequenze di valori.
'''

# Approccio tradizionale per creare una lista
lista_numeri = []

for i in range(10):
    lista_numeri.append(i)

print(lista_numeri)
print()

# list comprehension
listNumbers = [i for i in range(10)]
print(listNumbers)
print()

# set comprehension
setNumbers = {i for i in range(10)}
print(setNumbers)
print()

# dictionary comprehension
dictNumbers = {i: i * i for i in range(10)}
print(dictNumbers)
print()

'''
ATTENZIONE: la tuple comprehension NON esiste!
Un oggetto del tipo: (x for x in range(10)) si chiama generatore
'''
