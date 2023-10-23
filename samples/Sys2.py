# Usiamo il modulo argparse per il parsing dei parametri
import argparse
parser = argparse.ArgumentParser()  # inizializza parser

parser.add_argument('-n', '--nome_esteso', help='Descrizione del parametro')
parser.add_argument('-b', '--boolean_value', action='store_true', help="imposta il valore 'True' se trova il parametro")
parser.add_argument('-d', '--con_default', default='riferimento', help="Parametro che ha già un valore di default se non viene fornito l'argomento")
args = parser.parse_args()  # fa il parsing degli argomenti da linea di comando


print(args.nome_esteso)  # stampa a video il valore assegnato a nome_esteso
print(args.boolean_value)
print(args.con_default)

