#Atividade de laboratório 4 - Aula 04
#Autor: Rafael Sanzio
#Data: 28/08/17

import math

#Entrada
teatro = int(input("Digite o custo do espetáculo: "))
convite = int(input("Digite o valor do ingresso: "))

#Processamento
cobrir = teatro/convite
lucro = teatro*1.23/convite

#Saída
print("A quantidade de ingressos para cobrir o custo é",cobrir,"e para se ter um lucro de 23% são nescessário vender",lucro,)




