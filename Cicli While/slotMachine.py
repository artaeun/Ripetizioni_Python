import os
os.system("CLS")


# Marta va a un casino, e ci va con "n" gettoni
# Il casino ha 3 slot machine, e lei ci gioca in ordin
# finché non ha più gettoni
# Cioè, gioca alla prima slot machine, poi gioca alla
# seconda, poi alla terza, e poi di nuovo alla prima,ecc.

# Ogni giocata usa un gettone. 
# La slot machine funziona secondo queste regole:

# - la prima slot machine ti da 30 gettoni, ogni 35sima gioca
# - la seconda slot machine ti da 60 gettoni, ogni 100sima giocata
# - la terza slot machine ti da 9 gettoni ogni 10ma giocata.
# ogni altra giocata non si vince.

# determinare quante volte deve giocare Marta, affinché rimanga senza gettoni.


gettoni=int(input("Con gettoni entra nel casino Marta? : "))

giocata=0

while gettoni>0:

    giocata=giocata+1

    #slot machine 1
    if giocata%35==0:
        gettoni=gettoni+30
        print("Marta ha vinto 30 gettoni allo slot machine 1!")
        #print("Giocata: "+str(giocata)+"\nGettoni: "+str(gettoni)+"")
        #print("#"*50)
    else:
        gettoni=gettoni-1

    #slot machine 2
    if gettoni<1:
        print("Marta ha finito i gettoni con la slot machine 1")
        break

    if giocata%100==0:
        gettoni=gettoni+60
        print("Marta ha vinto 60 gettoni allo slot machine 2!")
        #print("Giocata: "+str(giocata)+"\nGettoni: "+str(gettoni)+"")
        #print("#"*50)
    else:
        gettoni=gettoni-1

    #slot machine 3
    if gettoni<1:
        print("Marta ha finito i gettoni con la slot machine 2")
        break

    if giocata%9==0:
        gettoni=gettoni+9
        print("Marta ha vinto 9 gettoni allo slot machine 3!")
        #print("Giocata: "+str(giocata)+"\nGettoni: "+str(gettoni)+"")
        #print("#"*50)
    else:
        gettoni=gettoni-1
   
    #print("Giocata: "+str(giocata)+"\nGettoni: "+str(gettoni)+"")
    #print("#"*50)

print("\nMarta ha finito di giocare in " +str(giocata)+" giocate.\n")