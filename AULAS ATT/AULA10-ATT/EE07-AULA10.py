#Faça um programa que receba a idade, a altura e o peso de 30 pessoas, calcule e mostre:
#a) a quantidade de pessoas com idade superior a 50 anos;
#b) a média das alturas das pessoas com idade entre 10 e 20 anos;
#c) a porcentagem de pessoas com peso inferior a 40 quilos entre todas as pessoas analisadas.

idade_50 = 0
menores = 0
peso_i = 0
sh = 0
porc = 0
media = 0

for i in range(4):
    print("PESSOA",i+1)
    idade = int(input("Digite a sua idade: "))
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite a sua altura: "))

    if idade > 50:    # PESSOAS COM IDADE MAIOR QUE 50 ANOS
        idade_50 += 1

    elif idade >= 10 and idade <= 20:   # MÉDIA DAS ALTURAS DAS PESSOAS DE 10 A 20 ANOS
        menores += 1  # SOMATÓRIO DE PESSOAS COM IDADE ENTRE 10 E 20
        sh = sh + altura # SOMÁTORIO DAS ALTURAS DESSAS PESSOAS
        media = sh/menores

    elif peso <= 40:     # PORCENTAGEM DE PESSOAS COM MENOS DE 40 KG
        peso_i += 1
        porc = (peso_i/4)*100

print("Do total analisado, as pessoas com mais de 50 são:",idade_50)
print("Do total analisado, a média das alturas das pessoas com 10 e 20 anos são:",format(media,".2f"))
print("Do total analisado, a porcentagem de pessoas com menos de 40kg são:",porc,"%")








