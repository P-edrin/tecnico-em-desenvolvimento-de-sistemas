numeros = []

for i in range(4):
    numeros.append(float(input(f"digite a {i+1}ª nota:")))

soma = sum(numeros)
print("soma total é: ", soma)
