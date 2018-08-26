#EXERCICIO EXTRA 01 - AULA 06

#TABELA
print("CELSIUS PARA FAHRENHEIT INFORME (F)\n""FAHRENHEIT PARA CELSIUS INFORME (C)")
print("NÃO SERÃO ACEITOS VALORES DIFERENTES DE F OU C""\n")

#ENTRADA
conv = input("Digite o tipo de conversão que você deseja fazer: ")
while conv.upper() != "F" and conv.upper() != "C":
    conv = input("Digite novamente!!!")

#CONDIÇÃO
if conv.upper() == "F": # CELSIUS PARA FAHRNEIT
    c = float(input("Digite o valor em celsius: "))
    conversão = c*1.8+32
    print("VALOR CONVERTIDO: ","F°",format(conversão,".2f"))

elif conv.upper() == "C": # FARHEREIT PARA CELSIUS
    f = float(input("Digite o valor em Farhneit: "))
    conversão = (f-32)/1.8
    print("VALOR CONVERTIDO: ", "C°",format(conversão, ".2f"))
