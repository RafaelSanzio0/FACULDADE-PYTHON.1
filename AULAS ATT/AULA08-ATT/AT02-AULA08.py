#ATIVIDADE DE LABORATÓRIO 02 - AULA 08

#ENTRADA/CONTADORES
alunos = int(input("Qual a quantidade de alunos?: "))
c_alunos = 0

#CONDIÇÃO
while c_alunos < alunos:
    n1 = float(input("NOTA 1: "))      # MEDIAS E NOTAS
    n2 = float(input("NOTA 2: "))
    n3 = float(input("NOTA 3: "))
    media = (n1+n2+n3)/3
    c_alunos = c_alunos + 1            # CONTADOR DE ALUNO

    if media >= 7.5:                   #CONDIÇÃO DE APROVADO OU REPROVADO
        print("A media do aluno foi de: ",format(media,".2f"))
        print("ALUNO APROVADO!!!")
    else:
        print("a media do aluno foi de: ",format(media,".2f"))
        print("ALUNO REPROVADO!!!")




