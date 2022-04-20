lista=[]

for i in range(10000):
    lista.append(i)

for i in range(len(lista)):
    if lista[i]>5000:
        print(lista[i])