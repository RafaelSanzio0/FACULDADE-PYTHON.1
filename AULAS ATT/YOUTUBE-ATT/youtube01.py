#FATORIAL

n = int(input("Digite o numero da serie: "))
fat = 1
print(n,"! = ",end="")

for i in range(n,0,-1):
    fat = fat * i
    if i == 1:
        print(i,end="")
    else:
        print(i,"x",end=" ")
print(" = ",fat)
