num1 = 10
num2 = 14
num3 = 12


if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
else:
    maior = num3

print("o maior numero entre %d,%d,%d é: %d" % (num1,num2,num3,maior))