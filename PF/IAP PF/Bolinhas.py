h = int(input("valor: "))
row = 0


while row < h:
    count = 0
    while count < h - row:
        print(end=" ")
        count += 1
    count = 0
    while count <2*row + 1:
        print(end="I")
        count += 1
    print()
    row += 1