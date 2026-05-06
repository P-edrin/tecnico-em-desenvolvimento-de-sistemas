# codigo sujo

a = float(input())
b = float(input())
c = float(input())
d = float(input())
x = (a + b + c  +d)/4

if x >= 7:
    print("OK")

elif x >= 5:
    print("REC")

else:
    print("NO")

#CLEAN CODE 1 
nota1 =float(input("digite a primeira nota: "))
nota2 =float(input("digite a primeira nota: "))
nota3 =float(input("digite a primeira nota: "))
nota4 =float(input("digite a primeira nota: "))

media = (nota1+nota2+nota3+nota4)/4

print("Sua media é: ",media)

if(media >= 7):
    print("aprovado")

elif(media >= 5):
    print("recuperação")

elif(media <5 ):
    print("reprovado!")
else:
    print("dados invalidos!")

#clean code 2
notas = []

for i in range(4):
    notas.append(float(input(f"digite a {i+1}ª nota:")))

media = sum(notas)/len(notas)

print("Sua media é: ",media)

if(media >= 7):
    print("aprovado")

elif(media >= 5):
    print("recuperação")

elif(media <5 ):
    print("reprovado!")
else:
    print("dados invalidos!")
