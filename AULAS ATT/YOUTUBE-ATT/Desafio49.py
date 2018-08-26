#DESAFIO 49
#TABUADA

n1 = int(input("Digite o numero inicial da tabuada: "))
n2 = int(input("Digite o numero de vezes: "))

for i in range(n1,n2+1):
    print("Tabuada do numero:",i)
    for j in range(n1,n2+1):
        print(i,"x",j,"=",i*j)
