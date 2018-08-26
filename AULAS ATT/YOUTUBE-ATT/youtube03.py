print("BEM VINDO AS ELEIÇÕES 2018""\n")
print("1-BOLSONARO / 2-DILMA / 3-LULA""\n")

eleitores = int(input("Numero total de eleitores é: "))
b = 0
d = 0
l = 0
total = 0

for i in range(eleitores):
    voto = int(input("Vote no seu candidato: "))
    while voto < 1 or voto > 3:
        voto = int(input("CANDIDATO NAO ENCONTRADO! DIGITE NOVAMENTE: "))
    if voto == 1:
        print("Voce votou no candidato JAIR BOLSONARO")
        b = b + 1
        total = b+d+l/eleitores

    elif voto == 2:
        print("Voce votou no candidato DILMA ROUSEFF")
        d = d + 1

    elif voto == 3:
        print("Voce votou no candidato LULA DA SILVA")
        l = l + 1

if b > d and b > l:
     print("BOLSONARO GANHOU AS ELEIÇÕES!!!")
elif d > b and d > l:
    print("DILMA GANHOU AS ELEIÇÕES!!!")
elif l > b and l > d:
    print("LULA GANHOU AS ELEIÇÕES!!!")
else:
     print("HÁ EMPATES, ENCAMIAREAMOS PARA O 2° TURNO OBRIGADO!")



print("BOLSONARO TEVE",b,"VOTOS")
print("DILMA TEVE",d,"VOTOS")
print("LULA TEVE",l,"VOTOS")











