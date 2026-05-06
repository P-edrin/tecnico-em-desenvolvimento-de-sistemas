lado1 = int(input("digite um lado1: "))
lado2 = int(input("digite um lado2: "))
lado3 = int(input("digite um lado3: "))

if(lado1+lado2>lado3 and lado1+lado3>lado2 and lado2+lado3>lado1 ):
    if(lado1 == lado2 and lado2 == lado3 and lado3== lado1):
        print("equilatero")
    elif(lado1 != lado2 and lado2 != lado3 and lado3 !=lado1):
        print("escaleno")
    else:
        print("isósceles")

else:
    print("o triangulo não existe!")
 