#EXERCICIO EXTRA 10 - AULA 05
#Autor: Rafael Sanzio
#Data: 31/08/2017

#Entrada
n = int(input("Digite um numero: "))
dez = n%100
dado = dez//10
if (dado%2)== 0:
    print("par")
else:
    print("impar")
    print("Dezena é,",dado)