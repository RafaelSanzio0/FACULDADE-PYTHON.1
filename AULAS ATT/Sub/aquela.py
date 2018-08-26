'''6.	Em	uma	competição	de	ginástica,	cada	atleta	recebe	votos	de	sete	jurados.	A	melhor	e	a	pior	nota	são	eliminadas.	A	sua	nota
fica	sendo	a	média	dos	votos	restantes.	Você	deve	fazer	um	programa	que	receba	o	nome	do	ginasta	e	as	notas	dos	sete	jurados
alcançadas	pelo	atleta	em	sua	apresentação	e	depois	informe	a	sua	média,	conforme	a	descrição	acima	informada	(retirar	o
melhor	e	o	pior	salto	e	depois	calcular	a	média	com	as	notas	restantes).	As	notas	não	são	informadas	ordenadas.	Um	exemplo
de	saída	do	programa	deve	ser	conforme	o	exemplo	abaixo:'''

#ENTRADA
nome = str(input("Atleta: "))
melhor = 0
pior = 0
media = 0
ac_nota = 0
nota_mediana = 0

#PROCESSAMENTO
for i in range(1,7+1):
    nota = float(input("nota: "))
    while nota < 0 or nota > 10:
        nota = float(input("dgt novamente (0 a 10): "))

    if i == 1:
        melhor = nota
        pior = nota

    else:
        if nota > melhor:
            melhor = nota

        if nota < pior:
            pior = nota

    if pior < nota and melhor > nota:
        continue
    else:
        nota_mediana += 1
        ac_nota += nota
        media = ac_nota/nota_mediana

#SAÍDA
print("-=-="*10)
print("Resultado final:")
print("Atleta:",nome)
print("Melhor nota:",melhor)
print("Pior nota:",pior)
print("Média:",format(media,".2f"))




