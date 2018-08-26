#DESAFIO 48
#NUMEROS IMPARES MULTIPLOS DE 3

cont = 0
soma = 0

for i in range(1,501,2):
    if i % 3 == 0:
        soma = soma + i
        cont += 1
print("A SOMA DE TODOS OS",cont,"VALORES SOLICITADO É",soma)
