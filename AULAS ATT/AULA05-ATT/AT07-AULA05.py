#ATIVIDADE DE LABORATÓRIO 07 - AULA 05

#ENTRADA
ano = int(input("Informe o ano: "))
preço = float(input("Informe o preço: "))

#CONDIÇÕES

if ano < 2010:
    taxa = preço * 0.25
    print("A taxa a ser paga é de: ""R$",taxa)
elif ano >= 2010:
    taxa = preço * 0.35
    print("A taxa a ser paga é de: ""R$",taxa)
