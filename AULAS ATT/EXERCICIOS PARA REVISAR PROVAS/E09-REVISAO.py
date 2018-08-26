'''9.	Dado	uma	string	com	uma	frase	informada	pelo	usuário
(incluindo	espaços	em	branco),	conte:
• quantos	espaços	em	branco	existem	na	frase.
• quantas	vezes	aparecem	as	vogais	a,	e,	i,	o,	u.'''

#ENTRADA
frase = str(input("Digite uma frase qualquer: "))

#PROCESSAMENTO
print("A Volga A aparece",frase.count("a"),"vezes")
print("A Vogal E aparece",frase.count("e"),"vezes")
print("A Vogal I aparece",frase.count("i"),"vezes")
print("A Vogal O aparece",frase.count("o"),"vezes")
print("A Vogal U aparece",frase.count("u"),"vezes")
print("A frase contém",frase.count(chr(32)),"espaços em branco")



