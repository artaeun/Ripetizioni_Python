import os
os.system('cls')




#definire una lista vuota:
listaVuota=[]
print(listaVuota)
print()

#definire una lista con elementi:
lista=[5,2,1,5,4,3,2]
print(lista)
print()

#visualizzare primo elemento della lista
print(lista[0])#il primo elemento ha sempre indice 0
print()

#visualizzare il secondo elemento della lista
print(lista[1])#il secondo ha indice 1, invece
print()

#visualizzare tutti gli elementi di una lista
print("Elementi della lista:")
for i in range(7):
    print(lista[i])
print()

#visualizzare in una sola riga tutti gli elementi di una lista
print("Elementi della lista:")
for i in range(7):
    print(lista[i], end=" $$ ")#puoi scegliere qualsiasi stringa da usare come fine di print
print()
print()

#fare somma di elementi di una lista definita
somma=0
for i in range(7):
    somma=somma+lista[i]
print("Somma è: "+str(somma))
print()


#ricavare il numero di elementi di una lista / la sua lunghezza:
lunghezzaLista = len(lista)
print(lunghezzaLista)
print()


#fare somma di elementi di una lista di lunghezza non definita
somma=0
for i in range(lunghezzaLista):
    somma=somma+lista[i]
print("Somma è: "+str(somma))
print()

# alternativa
somma=0
for i in range(len(lista)):
    somma=somma+lista[i]
print("Somma è: "+str(somma))
print()