print("------- menu de opeção -------")
print("1 - circulo")
print("2 - triangulo")
print("3 - Quadrado")
opcao = int(input("digite uma opção: "))

match opcao:
    case 1:
        print("⭕")
    case 2:  
        print("🔺")
    case 3:
        print("🟥")
    case _:
        print("❌ opção invalida!")