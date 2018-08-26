
n = int(input("Digite o numero da sequencia: "))
soma = 0

for i in range(n):
    print("Sequencia",i+1)
    n = int(input("Digite o numero da sequencia: "))
    soma = 0
    while n != 0:
        if n % 2 == 0:
            soma += n
            n = int(input("Digite o numero da sequencia: "))

        print("Numero da sequencia: ",i,"é",soma)

