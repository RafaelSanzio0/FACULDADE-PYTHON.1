#ATIVIDA DE LABORATÓRIO 03 - AULA 08
#AUTOR: RAFAEL SANZIO
#DATA: 22-09-17

#Entrada
alunos = int(input("Digite a quantidade de alunos: "))
cont_alunos = 1

#Processamento
while cont_alunos <= alunos: #CONTADOR DE ALUNOS
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    media =  (n1+n2+n3)/3
    cont_alunos = cont_alunos + 1
    print("A media do aluno foi: ", format(media, ".2f"))

#Saída
    if media >= 7.5:#CONDIÇÃO DE APROVADO OU REPROVADO
      print("Aluno aprovado!!!")
    else:
      print("Aluno reprovado!!!")


