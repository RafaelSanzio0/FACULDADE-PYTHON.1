#A série de Fibonacci é formada pela sequência 1, 1, 2, 3, 5, 8, 13, 21, 34, ... Escreva um
#programa que apresente a série de Fibonacci até o n-ésimo termo (n > 0).

n = int(input("Digie o numero da série: "))
u = 1
p = 1

print(p,",",u,end="")
for i in range(2,n,1):
    prox = u + p
    print(",",prox,end="")
    p = u
    u = prox


