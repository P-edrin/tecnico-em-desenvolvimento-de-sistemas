# sistemas de cadrastro de usuarios e produtos 
# o sistemas devera permitir:
# cadastrar
# listar 
# deletar 

# criação das listas
usuarios = []
produtos = []
#---------------------------
#----função menu usuarios----
def menu_usuarios():
    opcao_menu_usuarios = 0

    
    while(opcao_menu_usuarios != 4):
        print()
        print("----Menu usuarios----")
        print("1 - cadrastar usuarios")
        print("2 - listar usuarios")
        print("3 - deletar usuarios")
        print("4 - voltar")

        opcao_menu_usuarios = int(input("escolha uma opção: "))

        match opcao_menu_usuarios:
            #cadrastrar usuarios 
            case 1:
                nome = input("digite o nome: ")
                telefone = input("digite o telefone: ")
                email = input("digite o email: ")

                #criação do json de usuarios (chave: valor)
                usuario = {
                    "nome": nome,
                    "telefone": telefone,
                    "email": email
                }

                # adicionar o json no array
                usuarios.append(usuario)
                print(f"usuarios{usuario['nome']} cadratrar com sucesso!")
            case 2: 
                print("\n lista de usuarios: ")

                if(len(usuarios) == 0):
                    print("nenhum usuarios cadastrado!")
                else:
                    for usu in usuarios:
                        print("----------")
                        print("nome: ", usu["nome"])
                        print("telefone:", usu["telefone"])
                        print("email: ", usu["email"])
            #deletar usuarios 
            case 3:
                nome_deletar = input("digite o nome do usuario que deseja deletar:")
                encontrado = False

                for usu in usuarios:
                    if(usu["nome"] == nome_deletar):
                        usuarios.remove(usu)
                        encontrado = True
                        print("usuarios removidos com sucesso!")
                if(encontrado == False):
                    print("usuario não encontrado!")
                     
            # voltar ao menu principal
            case 4:
                print("voltando ao menu principal...")
                break
#----função menu produtos----
def menu_produtos():
    opcao_menu_produto = 0

    
    while(opcao_menu_produto != 5):
        print()
        print("----Menu produtos----")
        print("1 - cadrastar produtos")
        print("2 - listar produtos")
        print("3 - deletar produtos")
        print("4 - calcular total")
        print("5 - voltar")

        opcao_menu_produto = int(input("escolha uma opção: "))

        match opcao_menu_produto:
            #cadrastrar produto
            case 1:
                nome = input("digite o nome: ")
                descricao = input("digite o descrição: ")
                quantidade = int(input("digite o quantidade: "))
                valor = float(input("digite o valor:v"))

                #criação do json de produtos (chave: valor)
                produto = {
                    "nome": nome,
                    "telefone": descricao,
                    "email": quantidade,
                    "valor": valor
                }

                # adicionar o json no array
                produtos.append(produto)
                print(f"produto{produto['nome']} cadratrar com sucesso!")
            # listar produtos
            case 2: 
                print("\n lista de produto: ")

                if(len(produtos) == 0):
                    print("nenhum usuarios cadastrado!")
                else:
                    for pro in produto:
                        print("----------")
                        print("nome: ", pro["nome"])
                        print("descrição:", pro["descrição"])
                        print("quantidade: ", pro["quantidade"])
                        print("valor: ", pro["valor"])
            #deletar produto 
            case 3:
                nome_deletar = input("digite o nome do produto que deseja deletar:")
                encontrado = False

                for pro in usuarios:
                    if(pro["nome"] == nome_deletar):
                        usuarios.remove(pro)
                        encontrado = True
                        print("produto removidos com sucesso!")

                if(encontrado == False):
                    print("produto não encontrado!")
                     
            # voltar ao menu principal
            case 5:
                print("voltando ao menu principal...")
                break

#---------------------------
#------Menu principal------
opcao_menu = 0 
while(opcao_menu != 3):
    print("------Menu-Sitemas de cadrastro------")
    print("opções: ")
    print("1 - usuarios")
    print("2 - Produtos")
    print("3 - Sair")
    opcao_menu = int(input("escolha uma opção: "))

    match opcao_menu:
        #menu usuarios
        case 1:
            menu_usuarios()
        case 2:
            menu_produtos()
        case 3:
            print("até logo!")
        case _:
            print("opção invalida ")

