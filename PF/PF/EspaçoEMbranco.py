'''15.	Faça	um	programa	Python	que	receba	do	usuário	uma	frase	e	substitua	todos	os	espaços	em	branco	por	um	hífen.	Apresente
a	nova	frase	como	saída	da	execução.'''

#ENTRADA
frase = str(input("Digite uma frase: ")).split()

#PROCESSAMENTO
x = "-".join(frase)

#SAÍDA
print(x)
