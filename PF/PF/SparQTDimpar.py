''' Leia 30 números inteiros. Calcule e apresente a soma dos pares e a quantidade de ímpares'''

soma = 0
impares = 0

for i in range(30):
    if i % 2 == 0:
        soma += i
    else:
        impares += 1
print("soma dos pares",soma)
print("Qtd de impares",impares)
