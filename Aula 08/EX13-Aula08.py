#Exercicio 8 - Aul a08
#Rafael Sanzio

while True:

 print("Soma.....+")   #CATALOGO
 print("Subtração.....-")
 print("Multiplicação.....*")
 print("Divisão...../")
 print("Sair.....0\n")

 soma = "+" #VARIAVEIS
 subtração = "-"
 multiplicação = "*"
 divisão = "/"
 sair = "0"

 op = input("Digite a sua opçao: ") #ENTRADA

 if op == "+":                      #CONDIÇOES
    a = int(input("Informe A: "))
    b = int(input("Informe B: "))
    soma_a = a+b
    print("A soma é: ",soma_a,"\n")
 elif op == "-":
    a = int(input("Informe A: "))
    b = int(input("Informe B: "))
    subtração_a = a-b
    print("A subtração é: ",subtração_a,"\n")
 elif op == "*":
    a = int(input("Informe A: "))
    b = int(input("Informe B: "))
    multiplicação_a = a*b
    print("A multiplicação é: ",multiplicação_a,"\n")
 elif op == "/":
    a = int(input("Informe A: "))
    b = int(input("Informe B: "))
    divisão_a = a/b
    print("A divisão é: ",divisão_a,"\n")
 elif op == "0":
    print("Voce saiu do catalogo")
    break










