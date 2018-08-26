lower	=	0
upper	=	30
for	num	in	range(lower,upper	):
			#	prime	numbers	are	greater	than	1
			if	num	>	1:
							for	i	in	range(2,num):
											if	(num	%	i)	==	0:
															break
							else:
											print(num,end=",	")