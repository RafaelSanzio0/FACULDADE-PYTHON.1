#EXERCICIO EXTRA 08 - AULA 05

#ENTRADA
n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))

#CONDIÇÃO
if n1 > n2:
    maior = n1-n2
    print("A diferença é de: ",format(maior,".2f"))
elif n2 > n1:
    maior = n2-n1
    print("A diferença é de: ",format(maior,".2f"))
else:
    print("Numeros iguais diferença é 0")

