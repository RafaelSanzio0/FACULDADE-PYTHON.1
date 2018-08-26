''' Escreva um programa que receba N números reais, determine e apresente o maior valor.'''

maior = 0
menor = 0
qtd = int(input("qtd de testes: "))

for pessoa in range(qtd):
    print("pessoa",pessoa+1)
    peso = float(input("Peso: "))

    if pessoa == 1:
        maior = peso
        menor = peso

    if peso > maior:
         maior = peso
    else:
        menor = peso

print("maior peso",maior)
print("menor peso",menor)


