
import random
import os
os.system("cls")

nrElementi=2
lista=[]
print()
for i in range(nrElementi):
    lista.append(random.randint(0,50))
print(lista)


# media = (somma di tutti gli elementi)/(nr elementi)


somma=0

'''for i in range(nrElementi):
    valore=lista[i] #int(input())
    somma=somma+valore
'''
lista=[11,12,13,14,55,44,-1,54,1,41]

for i in range(10):
    valore=lista[i]
    somma=somma+valore

print("La somma dei valori della lista è:"+str(somma))
    