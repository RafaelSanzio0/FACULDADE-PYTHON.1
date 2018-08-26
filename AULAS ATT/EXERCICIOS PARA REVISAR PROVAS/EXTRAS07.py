''') Anacleto tem 1,50m e cresce 2 centímetros por ano, enquanto Felisberto tem 1,10m e cresce 3
centímetros por ano. Escreva um programa em Java que calcule e exiba quantos anos serão
necessários para que Felisberto seja maior que Anacleto'''

ana = 1.50
felis = 1.10
anos = 0
while  felis < ana:

    ana += 0.02
    felis += 0.03
    anos += 1
print("nescessarios",anos)