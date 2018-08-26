'''Escreva um algoritmo que calcule o valor de H, sendo que ele é determinado pela série
H = 1/1 + 3/2 + 7/4 + 11/6 + 15/8 + 19/10 + … + 99/50.
'''
import  math

n = int(input())
fatorial = math.factorial(n)
print(n,"!","=",fatorial)