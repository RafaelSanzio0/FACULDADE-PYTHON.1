#MOTSRAR OS MAIORES E MENORES DE IDADE

final = 0
cont_m = 0
cont_n = 0

for i in range(7):
    ano = int(input("Digite o seu ano de nascimento: "))
    final = 2017 - ano

    if final < 21:
        cont_n += 1
    else:
        cont_m += 1

print("MENOR DE IDADE SÃO: ",cont_n)
print("MAIORES DE IDADE SÃO: ",cont_m)









