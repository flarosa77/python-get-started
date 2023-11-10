def moreTimes(): # usa def per creare una funzione
  for i in range(0,50):
    print("Hello World!",'\n')

moreTimes()

'''Volendo decidere quante volte stampare a schermo lo stesso messaggio aggiungiamo un parametro di input'''

def moreTimes(num):
  for i in range(0,num):
    print("Hello World!",'\n')  

#moreTimes(10)

num = int(input('How many times you want repeat?\n'))

moreTimes(num)


'''Introduciamo una nuova funzione in grado di concatenare due stringhe '''

def concat(str1,str2):
 return str1 + ' ' + str2

str = concat('Marco','Rossi')

print(str)

'''Apportiamo una piccola modifica alla funzione precedente'''

def upAndConcat(str1,str2):
  return str1.upper() + ' ' + str2.upper()

str = upAndConcat('Marco','Rossi')

print(str)

'''Modifichiamo la funzione precedente introducendo la f-string'''
def upAndConcat2(str1,str2):
  return f"{str1.upper()} {str2.upper()}"
  
str = upAndConcat2('Marco','Rossi')

print(str)


#E di seguito qualche altro esempio di semplici funzioni

def sum(a, b):  
    return a + b


def factorial(a):
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result


def newprint(msg):
    print(msg)
    print()

def moreOps(a, b):
    c = a + b
    d = a - b
    return (c, d)




c = sum(10, 30)

print(c)

d = factorial(7)

print(d)

newprint("Hello world!")

tuple = (add, diff) = moreOps(10, 5)

print(add,'\n')
print(diff,'\n')
