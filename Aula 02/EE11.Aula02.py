#EXERCÍCIOS EXTRAS 11 - AULA 02
#Autor: Rafael Sanzio
#Data: 21/08/2017

#Entrada
area = float(input("Digite o M2 da área: "))

#Processamento
qtd_latas = area/54
preço = qtd_latas*80

#Saída
print("a quantidade de latas nescessária é:",format(qtd_latas,".0f"),"e preço a pagar vai ser:",format(preço,".2f"))
