# Usiamo il modulo "sys" per leggere i parametri passati all'applicazione tramite terminale
import sys

print(sys.argv)

# print(sys)

for argument in sys.argv:
    print(argument)
