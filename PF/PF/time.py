'''Uma pesquisa de opinião realizada em São Paulo teve três perguntas:
Pergunta 1:
Qual seu time do coração?
1-São Paulo
2- Corinthians
3-Santos
4-Outros
Pergunta 2:
Onde você mora?
1- São Paulo
2- Litoral
3- Interior
Pergunta 3:
Qual o seu salário?
a) Faça um programa Java que realize esta pesquisa com 15 pessoas.
b) Quando a pesquisa terminar, mostre o seguinte menu de opções:
1. Número de torcedores por clube
2. Média salarial dos torcedores do São Paulo
3. Número de pessoas moradoras de São Paulo, torcedoras do Corinthians
4. Número de pessoas do Litoral torcedoras do Santos
5. Sair.'''

print("TIMES/ 1- SÃO PAULO 2- CORINTHIAS 3- SANTOS 4- OUTROS")
print("RESIDÊNCIA/ 1- SÃO PAULO 2- LITORAL 3 - INTERIOR")
t_sp = 0
t_cr = 0
t_sa = 0
t_ou = 0
media = 0
salario_sp = 0
ac_salario = 0
pessoas_sp_cr = 0
pessoas_lt_sa = 0
cont = 0
pessoas = 5

while cont < pessoas:
    print("Pessoa",cont+1)
    time = int(input("Qual seu time do coração?: "))
    while time < 1 or time > 5:
        time = int(input("Dgt nov: "))
    morar = int(input("Onde você mora?: "))
    while morar < 1 or morar > 3:
        morar = int(input("Digite nov: "))
    salario = float(input("Qual seu salario?: "))
    cont += 1

    if time == 1: # torcedor sp
        t_sp += 1
        salario_sp += 1
        ac_salario += salario
        media = ac_salario/salario_sp

    elif time == 2: # torcedor cr
        t_cr += 1
        if morar == 1:
            pessoas_sp_cr += 1

    elif time == 3:
        t_sa += 1
        if morar == 3:
            pessoas_lt_sa += 1

    elif time == 4:
        t_ou += 1

print("Torcedores do SP",t_sp,"torcedores do CR",t_cr,"torcedores do SA",t_sa,"outros times",t_ou)
print("media do salario dos torcedores do SP",media)
print("Número de pessoas moradoras de São Paulo, torcedoras do Corinthians",pessoas_sp_cr)
print("Número de pessoas do Litoral torcedoras do Santos",pessoas_lt_sa)
