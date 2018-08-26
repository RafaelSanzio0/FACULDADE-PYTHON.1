#EXERCICIO TUTORADO 02 - AULA 06

#ENTRADA
a = int(input("Informe A: "))
b = int(input("Informe B: "))
c = int(input("Informe C: "))

#CONDIÇÕES
if a < b and a < c:
    print("O menor valor é A: ",a)
elif b < a and b < c:
    print("O menor valor é B: ",b)
elif c < a and c < b:
    print("O menor valor é C: ",c)
else:
    print("Existem valores iguais")