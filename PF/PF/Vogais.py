'''Dado	uma	string	com	uma	frase	informada	pelo	usuário	(incluindo	espaços	em	branco),	faça	um	programa	Python	que	conte
e	imprima:
• quantos	espaços	em	branco	existem	na	frase.
• quantas	vezes	aparecem	as	vogais	a,	e,	i,	o,	u.'''

#ENTRADA
frase = input().lower()

#SAÍDA
print("A frase contém %d vogal(s) A" % frase.count("a"))
print("A frase contém %d vogal(s) E" % frase.count("e"))
print("A frase contém %d vogal(s) I" % frase.count("i"))
print("A frase contém %d vogal(s) O" % frase.count("o"))
print("A frase contém %d vogal(s) U" % frase.count("u"))
print("A frase contém %d espaço(s)" % frase.count(" "))

#ENTRADA
frase = input().lower()
v = 0
c = 0

#PROCESSAMENTO
for i in range(len(frase)):

    if frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u":
        v += 1
    else:
        c += 1

#SAÍDA
print("A frase contém %d vogais e %d consoantes" % (v,c))