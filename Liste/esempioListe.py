
import random


mazzo=[]
for i in range(20):
    mazzo.append(random.randint(1,13))
print(mazzo)
print()

for carta in mazzo:
    print(carta) 

print("#"*30)

for i in range(0,20):
    print(mazzo[i])