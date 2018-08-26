#EXERCICIOS EXTRAS 01
#Autor: Rafael Sanzio
#Data: 21/08/2017

#Entrada
arquivo = float(input("Qual é o tamanho do arquivo que o senhor deseja fazer o donwload?: "))
link = float(input("Qual é a velocidade da sua internet?: "))

#Processamento
tempo = (link*8)/arquivo*60

#Sáida
print ("O tempo que resta para o seu download em minutos é: ",tempo)