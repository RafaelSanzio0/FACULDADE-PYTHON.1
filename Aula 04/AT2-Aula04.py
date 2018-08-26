#Atividade de laboratório 2 - Aula 04
#Autor: Rafael Sanzio
#Data: 28/08/17

import math

#Entrada
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

#Processamento
a = math.pow(n1,2)+math.pow(n2,2)+math.pow(n3,2)
b = math.pow(a,2)

#Saída
print ("Á soma dos quadrados dos três numeros são:",a,"e o quadrado desse numero é:",b)