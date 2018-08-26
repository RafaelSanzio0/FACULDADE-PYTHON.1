#ATIVIDADE DE LABORATÓRIO 02 - AULA 10

#Escreva um programa que apresente os n (1 <= n <= 20) primeiros termos da seguinte
#sequência: 1, 4, 9, 16, 25, ...

n = int(input("Digite o numero: "))
while n < 1 or n > 20:
    n = int(input("DIGITE NOVAMENTE!!!: "))

for i in range(n):
    print((n+1)**2)

