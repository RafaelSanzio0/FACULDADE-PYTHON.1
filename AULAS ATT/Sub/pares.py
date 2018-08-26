'''	Faça	um programa	Python	que	receba	do	usuário	uma	frase,	remova	os	caracteres	das	posições	pares	e	apresente	como
saída	a	nova	frase	gerada.
'''

frase = str(input("dgt a frase: "))

for i in range(len(frase)):

    if i % 2 == 0:
        continue

    else:
        remov = frase[i][::-1]
        print(remov,end="")







