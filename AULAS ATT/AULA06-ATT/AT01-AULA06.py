#ATIVIDADE DE LABORATÓRIO 01 - AULA 06

import random   #/ CHAMANDO A FUNÇÃO RANDOM
from time import sleep #/ CHAMANDO A FUNÇÃO SLEEP


#ENTRADA
aposta = int(input("Informe a sua aposta(1 a 12): "))
while aposta < 1 or aposta > 12:
    aposta = int(input("Digite novamente!!: "))
print("QUE OS JOGOS")
sleep(1)
print("COMEÇEM!!!""\n")

dado1 = random.randint(0,6)
dado2 = random.randint(0,6)

#PROCESSAMENTO
soma_dados = dado1 + dado2

#CONDIÇÃO
if soma_dados == aposta:
    print("Sua aposta foi:",aposta)
    print("A soma dos dados foram:",soma_dados)
    print("Você GANHOU!!!")
else:
    print("Sua aposta foi:", aposta)
    print("A soma dos dados foram:", soma_dados)
    print("Você PERDEU!!!")




