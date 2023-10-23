def somma(a, b):  # usa def per creare una funzione
    return a + b


def fattoriale(a):
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result


def stampa(msg):
    print(msg)
    print()


c = somma(10, 30)

print(c)

d = fattoriale(7)

print(d)

stampa("Hello world!")
