valor = int(input())
cedulas = 0
valoratual = 100
valorentregue = valor

while True:
    if valoratual <= valorentregue:
        cedulas += 1
        valorentregue -= valoratual
    else:
        print(cedulas,"de 100")
    if valorentregue == 0:
        break
    if valoratual == 100:
        valoratual == 100
        cedulas = 0






