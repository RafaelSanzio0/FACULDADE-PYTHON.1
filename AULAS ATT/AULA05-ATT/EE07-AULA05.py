#EXERCICIO EXTRA 07 - AULA 05

import math        #/ CHAMANDO A FUNÇÃO MATH

#ENTRADA
n = int(input("Digite o numero: "))

#CONDIÇÕES
if n >= 0:
    raiz = math.sqrt(n)
    print("A raiz quadrada do numero é: ",raiz)
elif n < 0:
    quadrado = math.pow(n,2)
    print("O quadrado do numero é: ",quadrado)

