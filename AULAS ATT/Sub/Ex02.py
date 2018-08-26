'''8.	Dado	uma	string	com	uma	frase	informada	pelo	usuário	(incluindo	espaços	em	branco),	faça	um	programa	Python	que	conte
e	imprima:
• quantos	espaços	em	branco	existem	na	frase.
• quantas	vezes	aparecem	as	vogais	a,	e,	i,	o,	u.'''

#ENTRADA
frase = str(input("Digite a frase: ")).upper()

#SAÍDA
print("Na frase informada temos",frase.count("A"),"Vogais da letra A")
print("Na frase informada temos",frase.count("E"),"Vogais da letra E")
print("Na frase informada temos",frase.count("I"),"Vogais da letra I")
print("Na frase informada temos",frase.count("O"),"Vogais da letra O")
print("Na frase informada temos",frase.count("U"),"Vogais da letra U")
print("Na frase informada temos",frase.count(" "),"Espaços em branco")