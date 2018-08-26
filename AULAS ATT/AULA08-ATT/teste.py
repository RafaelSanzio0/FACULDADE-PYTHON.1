n = int(input("Digie o numero da série: "))
u = 1
p = 1

print(p,",",u,end="") # ULTIMO E PENULTIMO NUMERO PRINTADO
for i in range(2,n,1): # 2 = NUMERO INICIANTE , N = NUMERO FINAL, 1 = SEQUENCIA
    prox = u + p       # MEU PROXIMO NUMERO VAI SER A SOMA DOS DOIS ULTIMOS
    print(",",prox,end="")
    p = u
    u = prox