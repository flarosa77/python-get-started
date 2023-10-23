import argparse

parser = argparse.ArgumentParser(prog="Sys3.py", description="Un programma che permette di gestire i parametri passati da terminale", epilog="Francesco La Rosa - 19/02/2022")


parser.add_argument('-n', '--nome_esteso', help='Descrizione del parametro')
parser.add_argument('-b', '--boolean_value', action='store_true', help="imposta il valore 'True' se trova il parametro")
parser.add_argument('-d', '--con_default', default='riferimento', help="Parametro che ha già un valore di default se non viene fornito l'argomento")


args = parser.parse_args()  # fa il parsing degli argomenti da linea di comando
print(args)  # stampa a video il valore assegnato a nome_esteso
