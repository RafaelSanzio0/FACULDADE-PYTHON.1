
termos = int(input("Dgt a qtd de termos: "))
s = 0

for i in range(1,termos+1):
    print((i/(termos-(i-1))),end="+")
    s = s + i/(termos-(i-1))

print("s =",s)

termos = int(input("termos: "))
s= 0
for i in range(termos):
    print(i/termos-(i-1))
    s = s + i/(termos-(i-1))
print(s)
