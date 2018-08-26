#EXERCICIO TUTORADO 03 - AULA 06

#TABELA
print("ARMAZENE O MENOR VALOR EM A\n""O INTERMEDIÁRIO NO B\n""O MAIOR EM C\n")


#ENTRADA
a = int(input("Informe A: "))
b = int(input("Informe B: "))
c = int(input("Informe C: "))

#CONDIÇÕES
if a < b and b < c:
    print("O valores em ordem crescente são: ",a,",",b,"e",c,)
else:
    print("Informe os valores de acordo com a tabela!")