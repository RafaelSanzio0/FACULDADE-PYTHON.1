#EXERCICIO EXTRA 02 - AULA 06

#APRESENTAÇÃO
print("        COMBUSTIVÉIS          ")
print("=-"*10)
print("A-álcool""\n""D-diesel""\n""G-gasolina")
print("=-"*10)

#ENTRADA
tipo = input("Digite o tipo de combustivel desejado: ")

#CONDIÇÕES
if tipo.upper() == "A": #ALCOOL
    litros = float(input("Qual a quantidade em litros?: "))
    preço = litros * 1.7997
    print("Valor total a pagar pelo álcool: ",format(preço,".2f"))

elif tipo.upper() == "D": #DIESEL
    litros = float(input("Qual a quantidade em litros?: "))
    preço = litros * 0.9798
    print("Valor total a pagar pelo diesel: ",format(preço, ".2f"))

elif tipo.upper() == "G": #GASOLINA
    litros = float(input("Qual a quantidade em litros?: "))
    preço = litros * 2.1009
    print("Valor total a pagar pela gasolina: ",format(preço, ".2f"))
else:
    print("TIPO INVÁLIDO!!!")



