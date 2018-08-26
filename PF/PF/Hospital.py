'''Um hospital precisa de um programa para calcular e imprimir os gastos de um paciente. A tabela
de preços do hospital é a seguinte:
 Quartos:
o Particular – R$ 360,00
o Semi-particular – R$ 210,00
o Coletivo – R$ 185,00
 WIFI: R$ 3,00
 TV a cabo: R$ 4,00
Escreva um programa que leia: o número de dias gastos no hospital; o tipo de quarto; se usou ou
não o WIFI (Sim, Não); se usou ou não a TV a cabo (Sim, Não). Então emita um relatório, como por
exemplo o seguinte:
Hospital Comunitário
Número de dias no hospital : 5
Tipo de quarto : Particular
Diárias :............... R$ 1800,00
WIFI :..... ....... R$ 3,00
TV a cabo :........... R$ 4,00
Total :................... R$ 1807,00'''

#ENTRADA
tipo = str(input("Tipo de quarto utilizado: "))
while tipo.upper() != "PARTICULAR" and tipo.upper() != "SEMI-PARTICULAR" and tipo.upper() != "COLETIVO":
  tipo = str(input("DIGITE NOVAMENTE, APENAS OS TIPOS DE QUARTOS DISPONIVEIS: "))


#PROCESSAMENTO
if tipo.lower() == "particular":
    dias = int(input("dias no quarto: "))
    wifi = str(input("usou wifi?: "))
    tv = str(input("usou tv?: "))
    diaria = dias * 360
    if wifi.upper() == "SIM":
        if tv.upper() == "SIM":
            total = diaria + 7
        if tv.upper() == "NAO":
            total = diaria + 3
    elif wifi.upper() == "NAO":
        if tv.upper() == "SIM":
            total = diaria + 4
        if tv.upper() == "NAO":
            total = diaria + 0
    print("TOTAL A PAGAR FOI DE: ",total)

if tipo.lower() == "semi-particular":
    dias = int(input("dias no quarto: "))
    wifi = str(input("usou wifi?: "))
    tv = str(input("usou tv?: "))
    diaria = dias * 210
    if wifi.upper() == "SIM":
        if tv.upper() == "SIM":
            total = diaria + 7
        if tv.upper() == "NAO":
            total = diaria + 3
    elif wifi.upper() == "NAO":
        if tv.upper() == "SIM":
            total = diaria + 4
        if tv.upper() == "NAO":
            total = diaria + 0
    print("TOTAL A PAGAR FOI DE: ",total)

if tipo.lower() == "coletivo":
    dias = int(input("dias no quarto: "))
    wifi = str(input("usou wifi?: "))
    tv = str(input("usou tv?: "))
    diaria = dias * 185
    if wifi.upper() == "SIM":
        if tv.upper() == "SIM":
            total = diaria + 7
        if tv.upper() == "NAO":
            total = diaria + 3
    elif wifi.upper() == "NAO":
        if tv.upper() == "SIM":
            total = diaria + 4
        if tv.upper() == "NAO":
            total = diaria + 0
    print("TOTAL A PAGAR FOI DE: ",total)