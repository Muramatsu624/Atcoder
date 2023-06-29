import math

N = int(input())

keta = len(str(N))

if(keta <= 3):
    print(N)
elif(keta <= 4):
    amari = N % 10**1
    print(N - amari)
elif(keta <= 5):
    amari = N % 10**2
    print(N - amari)
elif(keta <= 6):
    amari = N % 10**3
    print(N - amari)
elif(keta <= 7):
    amari = N % 10**4
    print(N - amari)
elif(keta <= 8):
    amari = N % 10**5
    print(N - amari)
elif(keta <= 9):
    amari = N % 10**6
    print(N - amari)

