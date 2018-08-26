#Atividade de laboratório 1 - Aula 04
#Autor: Rafael Sanzio
#Data: 28/08/17

import math

#Entrada
r = int(input("Digite o valor do raio: "))
h = int(input("Digite o valor da altura: "))

#Processamento
v = math.pi*math.pow(r,2)*h

#Saída
print("O volume da lata de óleo é:",v,"litros")