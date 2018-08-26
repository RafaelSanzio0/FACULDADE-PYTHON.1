'''xxx.xxx.xxx-xx'''

cpf = str(input("cpf: "))

p0 = cpf[0]
p1 = cpf[1]
p2 = cpf[2]
p4 = cpf[4]
p5 = cpf[5]
p6 = cpf[6]
p8 = cpf[8]
p9 = cpf[9]
p10 = cpf[10]
p12= cpf[12]
p13 = cpf[13]

if p0 < "a" or p0 > "z":
    print("cpf válido")
elif p1 < "a" or p1 > "z":
    print("cpf válido")
if p2 < "a" or p2 > "z":
    print("cpf válido")
if p4 < "a" or p4 > "z":
    print("cpf válido")
if p5 < "a" or p5 > "z":
    print("cpf válido")
if p6 < "a" or p6 > "z":
    print("cpf válido")
if p8 < "a" or p8 > "z":
     print("cpf válido")
if p10 < "a" or p10 > "z":
    print("cpf válido")
if p12 < "a" or p12 > "z":
    print("cpf válido")
if p13 < "a" or p13 > "z":
    print("cpf válido")
if p0 < "a" or p0 > "z":
    print("cpf válido")
else:
    print("cpf inválido")

