matriz1=[]
matriz2=[]
matriz_soma=[]

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Matriz1[{i}][{j}] = ")))
    matriz1.append(linha)
# PRENCHER MATRIZ (REPETIR SEMPRE QUE PRENCHER MATRIZ)
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"M2[{i}][{j}] = ")))
    matriz2.append(linha)

# PRENCHER MATRIZ (REPETIR SEMPRE QUE PRENCHER MATRIZ)
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(matriz1[i][j]+matriz2[i][j])
    matriz_soma.append(linha)

# EXIBIR MATRIZ (REPETIR SEMPRE QUE PRENCHER MATRIZ)
print("matriz soma: ")
for linha in matriz_soma:
    print(linha)


    