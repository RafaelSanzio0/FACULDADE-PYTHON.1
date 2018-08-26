#ATIVIDADE DE LABORATÓRIO 13 - AULA 08

#TABELA
print("SOMA..........+")
print("SUBTRAÇÃO.....-")
print("DIVISÃO......./")
print("MULTIPLICAÇÃO.*")
print("SAIR..........0""\n")

#ENTRADA
tipo = input("Escolha a opção desejada: ")
while tipo != "+" and tipo != "-" and tipo != "/" and tipo != "*" and tipo != "0":
    tipo = input("DIGITE UMA OPÇÃO VÁLIDA!: ")

#CONDIÇÃO
while tipo != "0":

    if tipo == "+":                   # SOMA
        n1 = int(input("NUMERO 1: "))
        n2 = int(input("NUMERO 2: "))
        soma = n1+n2
        print("Resultado da soma é:",soma)
        tipo = input("Escolha a opção desejada: ")
        while tipo != "+" and tipo != "-" and tipo != "/" and tipo != "*" and tipo != "0":
            tipo = input("DIGITE UMA OPÇÃO VÁLIDA!: ")

    elif tipo == "-":                # SUBTRAÇÃO
        n1 = int(input("NUMERO 1: "))
        n2 = int(input("NUMERO 2: "))
        sub = n1 - n2
        print("Resultado da subtração é:",sub)
        tipo = input("Escolha a opção desejada: ")
        while tipo != "+" and tipo != "-" and tipo != "/" and tipo != "*" and tipo != "0":
            tipo = input("DIGITE UMA OPÇÃO VÁLIDA!: ")

    elif tipo == "/":                # DIVISÃO
        n1 = int(input("NUMERO 1: "))
        n2 = int(input("NUMERO 2: "))
        div = n1 / n2
        print("Resultado da divisão é:",div)
        tipo = input("Escolha a opção desejada: ")
        while tipo != "+" and tipo != "-" and tipo != "/" and tipo != "*" and tipo != "0":
            tipo = input("DIGITE UMA OPÇÃO VÁLIDA!: ")

    elif tipo == "*":               # MULTIPLICAÇÃO
        n1 = int(input("NUMERO 1: "))
        n2 = int(input("NUMERO 2: "))
        mult = n1 * n2
        print("Resultado da multiplicação é:",mult)
        tipo = input("Escolha a opção desejada: ")
        while tipo != "+" and tipo != "-" and tipo != "/" and tipo != "*" and tipo != "0":
            tipo = input("DIGITE UMA OPÇÃO VÁLIDA!: ")

while tipo == "0":                  # SÁIDA
    print("Você saiu da calculadora")
    break




