'''Escreva um algoritmo que calcule e escreva a soma dos dez primeiros termos da seguinte série:
F = 2/500 – 5/250 + 2/400 – 5/350 + 2/300 – 5/450 +…'''


#ENTRADA
n1 = 500
n2 = 250
f= 0

#PROCESSAMENTO
for i in range(0,10):
    f += 2/n1
    f -= 5/n2
    n1 = 100
    n2 = 100
print(format(f,".6f"))
