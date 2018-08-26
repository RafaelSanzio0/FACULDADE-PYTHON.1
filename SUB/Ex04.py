#EXERCICIO 4

#ENTRADA
ac_idade = 0
ac_altura = 0
media = 0

#PROCESSAMENTO
for i in range(100):
    print("Pessoa",i+1)
    idade = int(input("Dgt a idade: "))
    peso = float(input("Dgt o peso: "))
    altura = float(input("Dgt altura: "))

    if idade > 60:
        ac_idade =+ 1

    ac_altura += altura
    media = ac_altura/100

#SAÍDA
print("Pessoas com idade superior a 60: ",ac_idade,"pessoas")
print("A media das alturas: ",format(media,".2f"))


