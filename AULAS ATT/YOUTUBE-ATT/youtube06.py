
#SOMA DE APENAS NUMEROS PARES

soma = 0
for i in range(6):
    n = int(input("Digite o numero: "))
    if n % 2 == 0:
        soma = soma + n
print("A SOMA DOS NUMEROS PARES DIGITADO É: ",soma)

