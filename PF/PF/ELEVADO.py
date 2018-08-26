'''.	Faça	um	programa	Python	que	determine	o	valor	da	série:	1	+	x^2/2	+	x^3/3	+	…	x^n/n. (Atenção:	x^3 é	x	elevado	a	3).	O
usuário	deve	informar	o	valor	de	x	e	o	número	de	termos	da	série	(n).'''

n = int(input("Qtd de termos: "))
x = int(input("Valor de X: "))

for i in range(2,n+2):
    serie =  (1 + x ** i )/ i
    print(" %d^%d/%d = " % (x,i,i,),end="")
    print(format(serie,".2f"))


