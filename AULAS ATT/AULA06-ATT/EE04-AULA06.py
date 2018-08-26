#EXERCICIO EXTRA 04 - AULA 06

#APRESENTAÇÃO
print("Olá senhor passageiro""\n")
print("Para vôo no período  noturno digite N""\n""Já para vôo no período diurno digite D""\n")

#ENTRADA
horario = input("Digite o horário do seu vôo de acordo com a tabela acima: ")

#CONDIÇÕES
if horario.upper() == "N":
    pessoas = int(input("Qual a quantidade de passageiros?: "))
    if pessoas <= 50:
        total = pessoas * 200
        print ("Total a pagar foi:","R$",total)
    if pessoas > 50:
        total = pessoas * 120
        print("Total a pagar foi:","R$",total)
elif horario.upper() == "D":
    pessoas = int(input("Qual a quantidade de passageiros?: "))
    if pessoas <= 50:
        total = pessoas * 100
        print("Total a pagar foi de:","R$",total)
    if pessoas > 50:
        total =  pessoas * 80
        print("Total a pagar foi de:","R$",total)
else:
    print("TIPO INVÁLIDO!!!")



