#ATIVIDADE DE LABORATÓRIO 03 - AULA 10

n = int(input("Informe N: "))
s= 0

for i in range(1,n+1):
    print(i/(n-(i-1)),end=" + ")
    s = s +(i/n-(i-1))
    print(s)
