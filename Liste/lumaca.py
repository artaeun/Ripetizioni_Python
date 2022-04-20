
lunghezzaPozzo=8
giorni=1

print()


if lunghezzaPozzo<=5:
    print("Ci mette un giorno")
else:
    for i in range(lunghezzaPozzo-5):
        giorni=giorni+1

    print("Ci mette",giorni,"giorni.")



print()