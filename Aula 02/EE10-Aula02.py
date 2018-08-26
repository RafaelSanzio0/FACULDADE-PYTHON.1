#EXERCÍCIOS EXTRAS 10 - AULA 02
#Autor: Rafael Sanzio
#Data: 01/09/2017

#Entrada
sal = float(input("Digite o salario de um funcionário: "))
percentual = float(input("Digite o percentual de aumento: "))

#Processamento
aumento = sal*percentual/100
novsal = sal+aumento

#Saída
print("o aumento foi de:",aumento,"e o novo salário é :",novsal)
