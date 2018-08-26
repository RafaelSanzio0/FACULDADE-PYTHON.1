'''Faça	um	programa	Python	que	determine	o	valor	da	série:	1	+	x^2/2	+	x^3/3	+	…	x^n/n. (Atenção:	x^3 é	x	elevado	a	3).	O
usuário	deve	informar	o	valor	de	x	e	o	número	de	termos	da	série	(n).'''

#ENTRADA
termos = int(input("Dgt a qtd de termos: "))
s = 0

for i in range(1,termos+1):
    print((i/(termos-(i-1))),end="+")
    s = s + i/(termos-(i-1))

print("s =",s)







