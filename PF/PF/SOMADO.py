#ATIVIDADE DE LABORATÓRIO 05 - AULA 8

#ENTRADA

n1 = int(input("Digite o valor de N1: ")) # VALOR A SER SOMADO
n2 = int(input("vezes: "))
soma = 0

for i in range(1,n2+1):
    soma += n1

    print(n1,end="+")

print("=",soma)
