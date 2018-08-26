#ATIVIDADE DE LABORATÓRIO 3 - AULA 02
#Autor: Rafael Sanzio
#Data: 01/09/2017

#Entrada
sal = float(input("Qual o valor do salario minímo: "))
agua = float(input("Qual foi a quantidade de água consumida no mês:"))

#Processamento
agua_cobrada = agua/1000
valor_pago = agua_cobrada*0.02*sal
valor_desconto = 0.85*valor_pago

#Saída
print ("O valor da conta de água é:",valor_pago,"com o desconto de 15% o novo valor será: ",format(valor_desconto,".2f"))

