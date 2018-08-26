#NUMEROS TRIANGULARES COM MULTIPLOS DE 5 DE 5 A 50:

#ENTRADA
for n in range(5,51,5):
    triangular = n*(n+1)//2
    print(n,"triangular é = ",triangular)