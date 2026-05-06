numeros = []
soma = 0
media=0
for i in range(6):
    numero=int(input("digite um numero:"))
    numeros.append(numero)
for numero in numeros:
   soma = soma + numero
media=soma/6
print(media)
