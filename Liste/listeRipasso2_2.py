import random
lista1=[]
lista2=[]

for i in range(10):
    lista1.append(random.randint(0,30))
    lista2.append(random.randint(0,30))

print(lista1)
print(lista2)

for i in range(10):
    for j in range(10):
        pass
        #print(lista1[i],"vs",lista2[j])
        #print("i:",i,"j:",j)
contatore=0
for elementoLista1 in lista1:
    for elementoLista2 in lista2:
        if elementoLista1==elementoLista2:
            contatore+=1

print("Conteggio:",contatore)