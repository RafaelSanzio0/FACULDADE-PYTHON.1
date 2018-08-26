#ATIVIDADE DE LABORATÓRIO 02 - AULA 06                             #CODIGO COM ERROS!!!

import random   #/ CHAMANDO A FUNÇÃO RANDOM

#ENTRADA
jogador = int(input("Informe um valor(0 a 10): "))
while jogador < 0 or jogador > 10:
    jogador = int(input("Digite novamente!!!: "))

maquina = random.randint(0,10)

#PROCESSAMENTO
soma = jogador + maquina

#CONDIÇÃO
if soma % 2 == 0: #CONDIÇÃO DE NUMERO PAR
    if jogador % 2 ==0:
        print("Jogador GANHOU!")
    else:
        print("Jogador PERDEU!")
    if maquina % 2 == 0:
        print("Maquina GANHOU!")
    else:
        print("Maquina PERDEU!")
elif soma % 2 !=0:            #CONDIÇÃO DE NUMERO IMPAR
    if jogador % 2 !=0:
        print("Jogador GANHOU!")
    else:
        print("Jogador PERDEU!")
    if maquina % 2 != 0:
        print("Maquina GANHOU!")
    else:
        print("Maquina PERDEU!")
else:
    print("EMPATE!!!")

print("JOGADOR ESCOLHEU O NUMERO: ",jogador)
print("A MAQUINA ESCOLHEU O NUMERO: ",maquina)
print("A SOMA DOS VALORES FORAM: ",soma)









