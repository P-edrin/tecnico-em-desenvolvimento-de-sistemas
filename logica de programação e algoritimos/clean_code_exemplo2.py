notas = []

for i in range(4):
    #tenta solicitar as notas
    try:
        nota = float(input(f"digite a {i+1}ª nota:"))

        if(nota < 0 or nota > 10):
            print("nota invalida. insira um valor dentre 0 e 10!")
            exit()
        else:
            notas.append(nota)
    # se tiver algum erro(excessão) de valor, retornar uma mensagem
    except ValueError:
        print("erro: insira um numero valido!")
    
#se a pessoa apenas digitou o texto
if not notas:
    print("erro: nenhuma nota foi insirida!")
else:
    media = sum(notas)/len(notas)

    if(media >= 7):
        print(f"media = {media} - aprovado!")
    elif(media >= 5):
        print(f"media = {media}- ecuperação")
    else:
        print(f"media = {media}- reprovado!")