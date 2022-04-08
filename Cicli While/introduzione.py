import os
os.system("CLS")


inputUtente=""

while inputUtente!="q":
    print("Vuoi sushi per cena? S/N")
    print("Inserire \"q\" per uscire dal programma")
    inputUtente= input("Inserire la tua opzione: ")

    if inputUtente=="S" or inputUtente=="s":
        print("Stasera si mangia sushi")
    elif inputUtente=="N" or inputUtente=="n":
        print("Stasera NON si mangia sushi")