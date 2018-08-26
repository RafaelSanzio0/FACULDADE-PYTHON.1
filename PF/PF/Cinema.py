'''Um cinema possui capacidade de 100 lugares e está sempre com ocupação total. Certo dia,
cada espectador respondeu a um questionário, no qual constava:
- sua idade (superior ou igual a 14 anos)
- sua opinião em relação ao filme, segundo as seguintes notas:
Nota Significado
A Ótimo
B Bom
C Regular
D Ruim
E Péssimo
Escreva um programa que, lendo esses dados, calcule e apresente:
a) a quantidade de respostas Ótimo;
b) a média de idade das pessoas que responderam Ruim;
c) a porcentagem de respostas Péssimo;
d) a maior idade entre as pessoas que responderam Bom;
e) a diferença entre a menor idade que respondeu Regular e a menor idade que respondeu
Ruim.'''

#ENTRADA
r_otimo = 0
ac_idade = 0
ac_media = 0
idade_r = 0
ac_pessimo = 0
maior = 0
menor_i = 0
menor_ri = 0
porc = 0
media = 0
menorr = 0

#PROCESSAMENTO
for i in range(4):
    print("pessoa",i+1)
    idade = float(input("idade: "))
    while idade < 14:
        idade = float(input("dgt nov: "))
    op = str(input("Opnião ao filme: "))

    if op.upper() == "A":
       print("Class Ótimo")
       r_otimo += 1

    elif op.upper() == "B":
       print("Class Bom")
       if idade == 1:
           maior = idade
       else:
           if idade > maior:
               maior = idade

    elif op.upper() == "C":
       print("Class Regular")
       if idade == 1:
           menor_i = idade
       else:
           if idade < menor_i:
               menor_i = idade

    elif op.upper() == "D":
        print("Class Ruim")
        idade_r += 1
        ac_idade = ac_idade + idade
        media =  ac_idade/idade_r

        if idade == 1:
            menor_ri = idade
        else:
            if idade < menor_i:
                menor_ri = idade

    elif op.upper() == "E":
        print("Class Péssimo")
        ac_pessimo += 1
        porc = (ac_pessimo/4)*100

    if menor_i < menor_ri:
        menorr = menor_ri - menor_i
    if menor_ri < menor_i:
        menorr = menor_i - menor_ri

#SAÍDA
print("a quantidade de respostas Ótimo",r_otimo)
print("a média de idade das pessoas que responderam Ruim",media)
print("a porcentagem de respostas Péssimo",porc,"%")
print("a maior idade entre as pessoas que responderam Bom",maior)
print("a diferença entre a menor idade que respondeu Regular e a menor idade que respondeu ruim",menorr)
