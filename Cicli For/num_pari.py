# prendere in input un numero (num), sommare i primi "num" 
# numeri pari e scrivere in output il risultato nel seguente modo:"Il risultato è X"

# Ad esempio, se num=4, X sarà 0+2+4+6=12

print("Inserire un numero da usare per i calcoli:")
num=int(input())
somma=0

for i in range(0,num):
    nrPari=i*2
    somma=somma+nrPari

print("Il risultato è", somma)
