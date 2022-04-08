# prendere in input un numero (num), sommare i primi "num" 
# numeri pari e scrivere in output il risultato nel seguente modo:"Il risultato è X"

# Ad esempio, se num=4, X sarà 0+2+4+6=12

print("Inserire un numero da usare per i calcoli:")
num=int(input())

numeroSommato=0
somma=0

contatoreSomma=1

while contatoreSomma<num:
    numeroSommato=numeroSommato+1

    if numeroSommato%2==0:
        somma=somma+numeroSommato

        contatoreSomma+=1

print(somma)