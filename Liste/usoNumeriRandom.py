import os
from random import randint
os.system('cls')

listaTiriDado=[]

for i in range(9):
    numeroRandom=randint(1,6)#tiro di un dado faccia 6
    listaTiriDado.append(numeroRandom)
    #print(numeroRandom)

print(listaTiriDado)
print("Lunghezza lista:", len(listaTiriDado))
#print()

somma=0
for i in range(len(listaTiriDado)):
    somma=somma+listaTiriDado[i]

print("La somma dei valori dei dadi tirati è: "+str(somma))