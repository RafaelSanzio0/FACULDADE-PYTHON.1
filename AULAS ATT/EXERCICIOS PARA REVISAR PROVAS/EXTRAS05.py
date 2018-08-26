''') Elabore um programa que receba a idade e a altura de várias pessoas, calcule e mostre a média
das alturas daquelas com mais de 50 anos. Para encerrar a entrada de dados, digite idade menor
ou igual a zero.
'''

pessoas = int(input("Qtd de pessoas: "))

maior_50 = 0
ac_altura = 0
media_50 = 0


for i in range(0,pessoas):
    print("Pessoa",i+1)

    idade = int(input("idade: "))
    if idade <= 0:
        print("programa encerrado")
        break

    altura = float(input("altura: "))

    if idade > 50:
        maior_50 += 1  #SOMA AS IDADES MAIOR QUE 50
        ac_altura += altura  # ACUMULA A ALTURA DESSES MAIOR QUE 50
        media_50 = ac_altura/maior_50  # FAZ A MEDIA

print("media",media_50)







