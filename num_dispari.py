# Prendere in input un numero (A) e sommare i primi A numeri dispari.
# Poi scrivere in output: "Il quadrato di A è X"

# A esempio, se A=5, allora X sarà uguale a:
# 1 + 3 + 5 + 7 + 9 = 25

A=int(input("Inserire A: "))
somma=0

for i in range(A):
    somma=somma+(i*2+1)

print("Il quadrato di",A,"è uguale a",somma)
