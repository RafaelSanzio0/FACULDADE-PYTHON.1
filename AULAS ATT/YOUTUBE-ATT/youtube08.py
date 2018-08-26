num = int(input('Digite um número inteiro qualquer: '))
cont = 0
for c in range(1,num+1):
    if num % c == 0:
        cont += 1
if cont == 2:
    print('O número {} é Prímo'.format(num))
else:
    print('O número {} Não é Prímo'.format(num))





