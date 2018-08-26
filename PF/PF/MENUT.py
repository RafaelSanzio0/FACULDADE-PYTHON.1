'''4.	 Escreva	 um	 programa	 que	 exiba	 uma	 lista	 de	 opções
(menu):	 adição,	 subtração,	 divisão,	 multiplicação	 e	 sair.
Imprima	a	tabuada	da	operação	escolhida.	Repita	até	que	a
opção	saída	seja	escolhida.
'''

#TABELA
print("\n""1-adição""\n""2-subtração""\n""3-divisão""\n""4-multiplicação""\n""5-saída""\n")

#OPÇÃO/CONTADORES/ACUMULADORES
op = int(input("Digite a opção desejada: "))
while op < 0 or op > 5:
    op = int(input("Digite uma opção válida: "))

#CONDIÇÕES/FOR/WHILE
while op != 5:
    if op == 1:
        n = int(input("informe o valor da tabuada a seguir: "))
        for i in range(1,11):
            print(n,"+",i,"=",n+i)

        op = int(input("Digite a opção desejada: "))
        while op < 0 or op > 5:
         op = int(input("Digite uma opção válida: "))

    elif op == 2:
        n = int(input("informe o valor da tabuada a seguir: "))
        for i in range(1,11):
            print(n,"-",i,"=",n-i)

        op = int(input("Digite a opção desejada: "))
        while op < 0 or op > 5:
         op = int(input("Digite uma opção válida: "))

    elif op == 3:
        n = int(input("informe o valor da tabuada a seguir: "))
        for i in range(1, 11):
            print(n, "/", i, "=", n/i)

        op = int(input("Digite a opção desejada: "))
        while op < 0 or op > 5:
         op = int(input("Digite uma opção válida: "))

    elif op == 4:
        n = int(input("informe o valor da tabuada a seguir: "))
        for i in range(1, 11):
            print(n, "x", i, "=", n*i)

        op = int(input("Digite a opção desejada: "))
        while op < 0 or op > 5:
         op = int(input("Digite uma opção válida: "))

while op == 5:
    print("voce saiu do menu")
    break
