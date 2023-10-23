import numpy as np

# Vettori
vettore = np.array([1, 2, 4, 3, 5])
print(vettore)
print(type(vettore))

print("Il minimo del vettore è: ", vettore.min())
print()

print("Il massimo del vettore è: ", vettore.max())
print()

mean = vettore.mean()

print("La media aritmetica del vettore è: ", mean)
print()

# Matrici
matrice = np.array([[0,0,0,1,0,0,0,0],
                    [0,0,0,0,0,0,1,0],
                    [0,0,1,0,0,0,0,0],
                    [0,0,0,0,0,0,0,1],
                    [0,1,0,0,0,0,0,0],
                    [0,0,0,0,1,0,0,0],
                    [1,0,0,0,0,0,0,0],
                    [0,0,0,0,0,1,0,0]])

print(matrice)
print(type(matrice))

