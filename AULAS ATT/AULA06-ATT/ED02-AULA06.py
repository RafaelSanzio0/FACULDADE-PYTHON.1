#EXERCICIO DISCUSSÃO EM DUPLA 01 - AULA 06

#ENTRADA
a = int(input("Informe A: "))
b = int(input("Informe B: "))
c = int(input("Informe C: "))

#CONDIÇÕES
if a < b+c and b < a+c and c < a+b:
    if a == b and b == c:
        print("Triangulo Equilátero")
    elif a == b or a == c or b == c:
        print("Triangulo Isósceles")
    elif a != b or b != c:
        print("Triangulo Escaleno")
else:
    print("Não é um triangulo!")
