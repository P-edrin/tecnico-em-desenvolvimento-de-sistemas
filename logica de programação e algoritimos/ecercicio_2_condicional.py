idade = int(input("digite sua idade: "))

if(idade >=0 and idade<=12):
    print(" crinça ")

elif(idade >=13 and idade<=17):
    print(" adolecente")

elif(idade >=18 and idade<=59):
    print(" adulto ")

elif(idade >= 60):
    print("idoso")

else:
    print("idade incorreta")