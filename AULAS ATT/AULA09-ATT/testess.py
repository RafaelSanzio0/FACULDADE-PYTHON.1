
n = int(input("enter any number: "))
sum1 = 0
for i in range(1,n):
 if(n % i == 0):
     sum1 += i
if (sum1==n):
    print("1")
else:
        print("2")