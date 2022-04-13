import random
import os

os.system("cls")

giornata=[]
for i in range(1000):
    temperatura=random.uniform(15, 28)
    giornata.append(temperatura)

media=giornata[0]
for i in range(1,len(giornata)):
    media=(media+giornata[i])/2


print(giornata)
print()
print()
print()
print(media)