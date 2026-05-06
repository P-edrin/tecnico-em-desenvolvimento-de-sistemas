matriz=[]
n=int(input("digite tamanho da matriz: "))

for i in range(n):
    linha = []
    for j in range(n):
        if(i==j):
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

print("matriz indentidade: ")
for linha in matriz:
    print(linha)