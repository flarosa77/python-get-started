'''Commento su più linee
da testare'''

# Commento su singola linea


# Importiamo keyword per mostrare a schermo l'elenco completo delle keyword di Python
# Usiamo il comando import per importare il modulo keyword
import keyword

# Stampiamo a schermo l'elenco delle keyword di Python (contenuto nella variabile kwlist)
print(keyword.kwlist)

# Usiamo la funzione type per determinare il tipo della variabile kwlist
# kwlist è una variabile di tipo (una classe) list (che approfondiremo in seguito)
print(type(keyword.kwlist))

# Approfondiamo la conoscenza della funzione print

# Stampiamo a schermo una stringa
print("Ciao")

# Inizializziamo la variabile "a"
a = 10

# Stampiamo a schermo il contenuto della variabile "a"
print(a)

# Scopriamo il tipo della variabile "a"
print(type(a))

# La variablie "a" è un oggetto di classe <int>


# Scopriamo il tipo della stringa 'ciao'
print(type('ciao'))
# 'ciao' è un oggetto di classe 'str'

# La funzione built-in di Python "len" applicata su una stringa restituisce
# la sua lunghezza (numero di caratteri)
print(len('parola'))


# Scriviamo una prima espressione
b = 5 * 6

# Stampiamo il contenuto della variabile b (risultato dell'espressione "5*6")
print(b)

# Come elevare al quadrato un numero/variabile?
b = 5**2

print(b)

print(7/3)  # divisione

print(7//3)  # divisione tra interi

print(7%3)  # resto della divisione tra interi (modulo)

# Concatenazione tra stringhe
string = 'ciao' + ' mondo '

# Un modo rapido per replicare (2 volte) una stringa
string2 = string*2

print(string)
print(string2)

# Funzioni per il casting

# Convertiamo un float in int
print(int(3.14))

# Conversione di un "int" in "str"
# Verifichiamo l'esito dell'operazione usando la funzione str()
print(type(str(3)))

# Conversione di un "int" in "float"
print(float(3))

# Confronto tra valori
m = 10
n = 10.0

print((m==n))

# Confronto tra tipi
print((type(m) == type(n)))

# Operazioni di input da terminale

# Acquisiamo un numero
num = input('Scrivi un numero\n')
print(num)

# Acquisiamo una stringa
nome = input('Nome?\n')

print('Ciao ' + nome + '\n')












