#TABUADA

começo = int(input("Digite o numero do começo: "))
fim = int(input("Digite o numero do fim: "))

#CONDIÇÃO FOR

for i in range(começo,fim+1):
    print("Para o numero",i)
    for j in range(começo,fim+1):
        print(i,"x",j,"=",i*j)

