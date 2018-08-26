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

if p0 < "A" or p0 > "z":
    print("cpf válido")
elif p1 < "A" or p1 > "z":
    print("cpf válido")
elif p2 < "A" or p2 > "z":
    print("cpf válido")
elif p4 < "A" or p4 > "z":
    print("cpf válido")
elif p5 < "A" or p5 > "z":
    print("cpf válido")
elif p6 < "A" or p6 > "z":
    print("cpf válido")
elif p8 < "A" or p8 > "z":
     print("cpf válido")
elif p10 < "A" or p10 > "z":
    print("cpf válido")
elif p12 < "A" or p12 > "z":
    print("cpf válido")
elif p13 < "A" or p13 > "z":
    print("cpf válido")
elif p0 < "A" or p0 > "z":
    print("cpf válido")
else:
    print("cpf inválido")