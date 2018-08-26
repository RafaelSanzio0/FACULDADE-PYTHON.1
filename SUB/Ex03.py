#EXERCICIO 3

#ENTRADA
termos = int(input("qtd de termos: "))
s = 0
c = 1
fracao = 0

#PROCESSAMENTO
for i in range(2,termos):
    s = 1+(c)/i
    fracao = s + s
    c += 2
    print(c,"/",i)

#SAÍDA
print("valor de S",fracao)



