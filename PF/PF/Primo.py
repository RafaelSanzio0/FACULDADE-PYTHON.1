n = int(input("numero: "))
m = 0
c = 0

for i in range(1,n+1):

    if n % i == 0:
        m += 1
    else:
        continue

if m == 2:
    print("é primo")
else:
    print("não é primo")
