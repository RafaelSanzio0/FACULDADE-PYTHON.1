#ENTRADA
alunos = int(input("Digite a qtd de alunos: "))
alunos_a = 0
alunos_r = 0
menor = 0
maior = 0
mediag = 0
ac_media = 0
ac_nota = 0

for i in range(alunos):
    print("aluno",i+1)

    matricula = int(input("matricula: "))
    if matricula == 0:
        print("Sistema encerrado")
        break

    n1 = float(input("NOTA 1: "))
    n2 = float(input("NOTA 2: "))
    n3 = float(input("NOTA 3: "))

    frequencia = float(input("frequencia nas aulas: "))

#PROCESSAMENTO
    media = (n1+n2+n3)/3 # media de um aluno


    if media >= 6.0 and frequencia > 40:
        alunos_a += 1
        print("Aprovado")
    else:
        alunos_r += 1
        print("Reprovado")

    if n1 == 0 and n2 == 0 and n3 == 0:
        menor = n1,n2,n3
        maior = n1,n2,n3

    if n1 > maior or n2 > maior or n3 > maior:
        maior = n1 or n2 or n3
    else:
        menor = n1 or n2 or n3

#SAÍDA
print("maior",maior)
print("menor",menor)


















