'''	 O	 Departamento	 Estadual	 de	 Meteorologia	 lhe	 contratou	 para	 desenvolver	 um	 programa	 que	 leia	 as	 um	 conjunto
indeterminado	 de	 temperaturas,	 e	 informe	 ao	 final	 a	 menor	 e	 a	 maior	 temperatura	 informada,	 bem	 como	 a	 média	 das
temperaturas. Escreva	um	programa	Python	para	resolver	o	problema.'''

#ENTRADA
qtd = int(input("Informe a quantidade de temperaturas: "))
ac_temp = 0
menor = 0
maior = 0


#PROCESSAMENTO
for i in range(qtd):
    print("Temperatura",i+1)
    temp = float(input("Digite: "))

    if i == 0:
        menor = temp
        maior = temp

    else:
        if temp < menor:
            menor = temp
        if temp > maior:
            maior = temp

    ac_temp += temp
    media = ac_temp/qtd

#SAÍDA
print("A menor temperatura:",menor)
print("A maior temperatura:",maior)
print("A media das temperaturas:",format(media,".2f"))
