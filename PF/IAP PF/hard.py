

texto	=	"Exercicios	da	Logica"
cont	=	0
n	=	1
for	i	in	range(len(texto)):
				if	texto[i]	==	"	":
								break
				else:
								cont	+=	1
								print(texto[i],end="")
print("	",end="")
for	j	in	range(len(texto)-1,	cont,	-1):
				 print(texto[j],end="")