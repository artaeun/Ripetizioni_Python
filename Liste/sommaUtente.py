# utente inserisce 5 valori
# calcolare la somma dei 5 valori

somma=0

listaValori=[1,4,4,7,4]

for i in range(5):
    print("Inserire valore: ")
    #valore=int(input())
    valore=listaValori[i]
    somma=somma+valore
    print("Somma="+str(somma))


print("La somma dei valori inseriti è: "+str(somma))