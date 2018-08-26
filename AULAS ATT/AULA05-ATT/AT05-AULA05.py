#ATIVIDADE DE LABORATÓRIO 05 - AULA 05

#ENTRADA
ano = int(input("Informe o ano: "))

#CONDIÇÕES
if ano % 4 == 0:
    print("O ano é bissexto")
elif ano % 400 == 0:
    print("O ano é bissexto")
else:
    print("O ano informado não é bissexto")