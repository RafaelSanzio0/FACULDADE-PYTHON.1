#EXERCICIO EXTRA 10 - AULA 05

#ENTRADA
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

#PROCESSAMENTO
media = (n1*2+n2*3+n3*5)/10

#CONDIÇÃO
if media >= 6.0:
    print("Aluno aprovado!","media",format(media,".2f"))
else:
    print("Aluno reprovado!","media",format(media,".2f"))