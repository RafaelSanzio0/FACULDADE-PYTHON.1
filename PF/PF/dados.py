'''Leia um conjunto de dados contendo a altura (de 1,00 m a 2,30 m) e o sexo (F ou M) de n
(1 <= n <= 50) pessoas. Calcule e apresente:
a) a maior e a menor altura do grupo;
b) a média de altura das mulheres;
c) o número de homens.'''

#ENTRADA
maior = 0
menor = 0
media = 0
homens = 0
ac_altura = 0
id_m = 0
ac_homens = 0


#PROCESSAMENTO
qtd = int(input("Informe a qtd de pessoas: "))

for i in range(qtd):
    print("Pessoa",i+1)

    altura = float(input("altura: "))
    while altura < 1.00 or altura > 2.30:
        altura = float(input("dgt nov: "))

    sexo = str(input("sexo: "))
    while sexo.upper() != "F" and sexo.upper() != "M":
        sexo = str(input("dgt nov: "))

    if altura == 0:
        maior = altura
        menor = altura
    else:
        if altura > maior:
            maior = altura
        if altura < menor:
            menor = altura

    if sexo.upper() == "F":
        id_m += 1
        ac_altura += altura
        media = ac_altura/id_m

    else:
        ac_homens += 1

print("maior altura ",maior,"menor altura ",menor)
print("media de altura das mulheres",media)
print("numero de homens ",ac_homens)