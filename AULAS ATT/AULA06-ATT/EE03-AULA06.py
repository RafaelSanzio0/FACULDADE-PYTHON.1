#EXERCICIO EXTRA 03 - AULA 06

#ENTRADA
saldo = float(input("Qual foi o seu saldo médio no ultimo ano: "))

#CONDIÇÕES
if saldo > 4000:
    perc = saldo * 0.30
    print("Crédito especial de:",format(perc,".2f"))

elif saldo > 3000 and saldo <= 4000:
    perc = saldo * 0.25
    print("Crédito especial de:",format(perc,".2f"))

elif saldo > 2000 and saldo <= 3000:
    perc = saldo * 0.20
    print("Crédito especial de:",format(perc,".2f"))

elif saldo <= 2000:
    perc = saldo * 0.10
    print("Crédito especial de:",format(perc,".2f"))

