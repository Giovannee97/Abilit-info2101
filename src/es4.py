import numpy as np

A=np.loadtxt("MATRICE.txt",dtype="i",delimiter=None)

print(A)

Autovalori=np.linalg.eigvals(A)
print("Autoval",Autovalori)
Autovettori=np.linalg.eig(A)
print("Autovect",Autovettori)
