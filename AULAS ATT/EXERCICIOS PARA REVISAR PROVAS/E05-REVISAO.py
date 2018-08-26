'''5.	O	Departamento	Estadual	de	Meteorologia	lhe	contratou
para	 desenvolver	 um	 programa	 que	 leia	 as	 um	 conjunto
indeterminado	de	temperaturas,	e	informe	ao	final	a	menor
e	a	maior	 temperatura	informada,	bem	como	a	média	das
temperaturas.'''

#ENTRADA/CONT/ACUM
qtd = int(input("Informe a quantidade de temperaturas que deseja: "))
maiort = 0
menort = 0
ac_temp = 0
media = 0

#LOOP
for i in range(qtd):
    temp = float(input("Digite a tempatura: "))

    if i == 0:
        maiort = temp
        menort = temp
    else:
        if temp > maiort:
            maiort = temp
        if temp < menort:
            menort = temp

    ac_temp += temp
    media = ac_temp / qtd

print("Menor temperatura:",menort)
print("Maior temperatura:",maiort)
print("A media das temperaturas é:",media)








