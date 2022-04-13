from random import randint

from scipy import rand
import os

os.system("cls")

giorni=7
temperatureGiorni=[]

for i in range(giorni):
    temperaturaOggi=randint(20,35)
    temperatureGiorni.append(temperaturaOggi)

print(temperatureGiorni)
print()

for i in range(len(temperatureGiorni)):
    print("La temperatura il giorno "+str(i+1)+" era di "+str(temperatureGiorni[i])+"°C.")

print()