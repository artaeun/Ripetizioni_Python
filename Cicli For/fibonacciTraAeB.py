# Prendere in input 2 numeri (A e B) e visualizzare i valori della
# successione di Fibonacci compresi nell'intervallo chiuso [A,B]
# A esempio, se A=7, B=40, leggeremo in output: 8 13 21 34

#print("Inserire il numero di Fibonacci da calcolare: ")
#numeroDiFibonacciDaCalcolare=int(input())

A=int(input("Inserire A: "))
B=int(input("Inserire B: "))

f0=0
f1=1

fib=0

#0 1 1 2 3 5 8 13 21 34 55 ecc
for i in range(B):
    fib=f0+f1
    
    f0=f1
    f1=fib

    if fib>A and fib<B:
        print(fib,end=" ")

    if fib>B:
        break


#alternativa con While
'''while fib<B:
    fib=f0+f1
    f0=f1
    f1=fib
    if fib>A and fib<B:
        print(fib,end=" ")'''