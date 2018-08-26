#Atividade de laboratório 3 - Aula 04
#Autor: Rafael Sanzio
#Data: 28/08/17

import math

#Entrada
data = (input("Digite a data de nascimento no formato aaaa/mm/dd: "))

#Processamento
ano = data[0]+data[1]+data[2]+data[3]
mes = data[4]+data[5]
dia = data[6]+data[7]

#Saída
print ("A data de nascimento no formato dd/mm/aaaa è: ",dia,"/",mes,"/",ano)