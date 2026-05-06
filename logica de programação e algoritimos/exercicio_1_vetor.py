numeros = []
conta_pares=0
for i in range(10):
    numero=int(input("digite um numero:"))
    numeros.append(numero)
for numero in numeros:
    if(numero%2==0):
        conta_pares=conta_pares+1
print(conta_pares)
