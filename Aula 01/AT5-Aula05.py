#ATIVIDADES DE LABORATÓRIO 05 - AULA 01
#Autor: Rafael Sanzio
#Data: 01/09/2017

#Entrada
s = float(input("Quanto você ganha por hora trabalhada: "))
h = float(input("Quantas horas você trabalha por mês: "))

#Processamento
st = s*h

#Saída
print("Você ganha por hora",s,"e trabalha",h,"horas por mês, no total você irá ganhar no fim do mes",format(st,".2f"))