import random

lista1=[]
lista2=[]

for i in range(0,10):
    lista1.append(random.randint(0,30))
    lista2.append(random.randint(0,30))

print("Lista 1: ",lista1)
print("Lista 2: ",lista2)


contatore=0
for i in range(0,10):
    for j in range(0,10):
        print("lista1[i]:",lista1[i]," vs ", "lista2[j]:",lista2[j])
        if lista1[i]==lista2[j]:
            print("Valori sono uguali")
            print("#"*40)
            contatore=contatore+1


print("Sono state trovate",contatore,"valori uguali nelle due liste")