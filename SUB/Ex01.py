#EXERCICIO 01

#ENTRADA
alunos = int(input("Qtd de alunos na sala: "))

#PROCESSAMENTO
for i in range(alunos):
    print("aluno",i+1)
    n1 = float(input("NOTA1: "))
    n2 = float(input("NOTA2: "))
    media = (n1+n2)/2

#SAÍDA
    if  media > 7.5:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado, deve fazer a SUB")



