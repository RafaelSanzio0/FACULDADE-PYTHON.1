#EXERCICIO 2

#ENTRADA
valor_i = int(input("Digite o valor inicial: "))
valor_f = int(input("Digite o valor final: "))
soma = 0

#PROCESSAMENTO
for i in range(valor_i,valor_f):

    if i % 2 == 0:
        continue

    else:
      soma = soma + i

#SAÍDA
print("A SOMA DOS NUMEROS IMPARES DENTRO DA SEQUENCIA  É: ",soma)