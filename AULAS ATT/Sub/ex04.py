'''18.	Faça	um	programa	que	receba	a	idade,	a	altura	e	o	peso	de	30	pessoas,	calcule	e	mostre:
a)	 a	quantidade	de	pessoas	com	idade	superior	a	30	anos;
b) a	média	das	alturas	das pessoas	com	idade	entre	10	e	25 anos;
c) a	porcentagem	de	pessoas	com	peso	inferior	a	50	quilos	entre	todas	as	pessoas	analisadas.
d) a	média	da	idade	das	pessoas
e) quantas	pessoas	tem	obesidade mórbida'''

#ENTRADA
id30 = 0
alt_10_25 = 0
ac_altura = 0
peso50 = 0
media_10_25 = 0
obesos = 0
ac_idade = 0
mediaid = 0

for i in range(30):
    print("Pessoa",i+1)
    idade = int(input("Idade: "))
    altura = float(input("Altura: "))
    peso = float(input("Peso: "))
    print("-=-="*10,"\n")

#PROCESSAMENTO
    if idade > 30:
        id30 += 1

    if idade >= 10 and idade <= 25:
        alt_10_25 += 1
        ac_altura += altura
        media_10_25 = ac_altura/alt_10_25

    if peso < 50:
        peso50 += 1
        porc = (peso50/30)*100

    if peso > 150:
        obesos += 1

    ac_idade += idade
    mediaid = ac_idade/30

#SAÍDA
print("a quantidade de pessoas com idade superior a 30 anos ",id30)
print("a média	das	alturas	das pessoas	com	idade entre	10 e 25 anos ",media_10_25)
print("a porcentagem de pessoas	com	peso inferior a	50 quilos entre	todas as pessoas analisadas ",porc,"%")
print("a média da idade das	pessoas ",mediaid)
print("quantas pessoas tem obesidade mórbida ",obesos)











