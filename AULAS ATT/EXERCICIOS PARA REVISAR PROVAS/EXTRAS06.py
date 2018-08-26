
#ENTRADA
qtd = int(input("Digite a qtd de testes: "))
soma = 0
qtd_n = 0
ac_numero = 0
soma_p = 0
qtd_nn = 0
media_p = 0
ac_par = 0
ac_impar = 0
media = 0
impares = 0

#PROCESSAMENTO
for i in range(0,qtd):
    print("NUMERO",i+1)
    numero = float(input("Digite o numero: "))

    soma += numero # A

    qtd_n += 1     # B

    ac_numero += numero
    media = ac_numero/qtd_n # C

    if numero > 0:   # D
        soma_p += numero

    if numero < 0:  # E
        qtd_nn += 1

    if numero % 2 == 0:
        ac_par += numero
        media = ac_par/qtd_n # F

    if numero % 2 == 0:   # G
        continue
    else:
        ac_impar += 1
        impares = (ac_impar *numero)/100

#SAIDA
print("Soma dos numeros digitados: ",soma)
print("a quantidade de números digitados",qtd_n)
print("a média dos números digitados",media)
print("a soma dos números positivos",soma_p)
print("a quantidade de números negativos",qtd_nn)
print("a média dos números pares",media)
print("o percentual dos números ímpares entre todos os números digitados",impares,"%")






























