
somma=0
temperature=[]


for i in  range(7):
    temperatura=float(input())
    somma=temperatura+somma

    temperature.append(temperatura)

print()
print("Temperatura totale: "+str(somma))
print(temperature)

min=0
max=0
for i in range(7):
    t=temperature[i]
    if i==0:
        min=t
        max=t
    else:
        if t>max:
            max=t
        elif t<min:
            min=t

print("Max:",max)
print("Min:",min)