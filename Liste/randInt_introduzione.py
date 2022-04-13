import os
from random import randint

os.system("cls")

lista=[]
print()
for i in range(10):
    x=randint(1,10)
    lista.append(x)
print(lista)

lunghezzaLista=len(lista)
print(lunghezzaLista)

print()

somma=0
for i in range(0,lunghezzaLista):
    somma=somma+lista[i]

print(somma)