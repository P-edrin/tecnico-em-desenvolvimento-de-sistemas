num1 = int(input("digite um numero: "))
num2 = int(input("digite um numero: "))
soma = 0 
for i in range(num1,num2,+1):
    if(i%2 == 0):
     soma = soma +i 
print("soma é:", soma )