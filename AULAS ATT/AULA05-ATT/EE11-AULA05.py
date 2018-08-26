#EXERCICIO EXTRA 11 - AULA 05

#ENTRADA
peso = float(input("Digite o peso de peixes: "))

#CONDIÇÃO
if peso > 50:
    multa = (peso-50)*4
    print("O valor da multa a pagar é: ","R$",multa)
else:
    print("Dentro do regulamento")