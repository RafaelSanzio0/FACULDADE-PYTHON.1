#EXERCICIO EXTRA 10 - AULA 05
#Autor: Rafael Sanzio
#Data: 31/08/2017

#Entrada
n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))
n3 = int(input("Digite a terceira nota: "))

#Processamento
media = ((n1*2)+(n2*3)+(n3*5))/10

#Saída
print ("A media é: ",media,)

if media >=6:
    print ("Aluno aprovado!")
else:
    print ("Aluno reprovado!")


