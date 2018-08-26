'''Em um campeonato de futebol existem cinco times e cada um possui onze jogadores. Faça um
algoritmo que receba a idade (de 14 a 35), o peso (de 60.0 a 100.0) e a altura (de 1.60 a 2.00)
de cada um dos jogadores, calcule e mostre:
a) a quantidade de jogadores menores de idade (idade inferior a 18 anos);
b) a média das idades dos jogadores de cada time;
c) a média das alturas de todos os jogadores do campeonato;
d) a porcentagem de jogadores com mais de 80Kg entre todos os jogadores do campeonato.'''


time = 2
jogadores = 4
menor_18 = 0

for i in range(time):
    for j in range(jogadores):

        idade = int(input("Digite a idade: "))
        while idade < 14 or idade > 35:
            idade = int(input("Digite novamente: "))

        peso = float(input("Digite o peso: "))
        while peso < 60 or peso > 100:
            peso = float(input("Digite novamente: "))

        if idade < 18:
            menor_18 += 1






