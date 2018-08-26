'''8.	Faça	um	programa	que	receba	a	idade,	a	altura	e	o	peso	de	30	pessoas,	calcule	e	mostre:
a)	 a	quantidade	de	pessoas	com	idade	superior	a	30	anos;
b) a	média	das	alturas	das pessoas	com	idade	entre	10	e	25 anos;
c) a	porcentagem	de	pessoas	com	peso	inferior	a	50	quilos	entre	todas	as	pessoas	analisadas.
d) a	média	da	idade	das	pessoas
e) quantas	pessoas	tem	obesidade mórbida'''


id30 = 0
ac_alt = 0
alt10_25 = 0
peso50 = 0
ac_id = 0
ob = 0
media = 0
media_a = 0
porc = 0

for i in range(5):
	print("pessoa",i+1)
	id = int(input("idade: "))
	alt = float(input("altura: "))
	peso = float(input("peso: "))

	if id > 30:
		id30 += 1

	if id > 10 and id < 25:
		alt10_25 += 1
		ac_alt += alt
		media_a = ac_alt/alt10_25

	if peso < 50:
		peso50 += 1
		porc = (peso50/5)*100

	if peso > 150:
		ob += 1

	ac_id += id
	media = ac_id/5

print("Maiores que 30 anos",id30)
print("Media da altura das pessoas de 10 a 25 anos",media_a)
print("porcetagem dos que pesam menos que 50 kilos",porc)
print("media da idade das pessoas",media)
print("Qtd de obesos morbidos",ob)





