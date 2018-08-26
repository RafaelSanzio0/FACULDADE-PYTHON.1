#ATIVIDADE DE LABORATÓRIO 04 - AULA 10

#ENTRADA
n = int(input("Digite o valor do fatorial: "))
fat = 1

#CONDIÇÃO
for i in range (1,n+1):
    fat = fat * i
print(n,"!","=",fat)