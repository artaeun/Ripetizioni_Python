# Prendere in input un numero "num" e sommare i multipli di "num" compresi tra 20 e 80

print("Inserire num:")
num=int(input())
somma=0


for i in range(21,80):
    if i%num==0:
        somma=somma+i

print("Il risultato è", somma)
