# Un cinema sta facendo un sondaggio riguardante l'eta dei propri clienti
# Scrivere un programma che prenda in input l'età di 6 clienti
# contare quanti di questi sono sotto ai 25 anni
# tra i 25 e 40 anni, e quanti sopra ai 40
sotto25=0
tra25e40=0
sopra40=0

for i in range(6):
    print(str(i+1)+") Inserire la propria eta':")
    eta=int(input())
    if eta<25:
        sotto25+=1
    elif eta>40:
        sopra40+=1
    else:
        tra25e40+=1


print("\nClienti sotto i 25 anni:",sotto25)
print("Clienti tra i 25 e 40 anni:",tra25e40)
print("Clienti sopra i 40 anni",sopra40)

