import json

estoque = {
    'Titulo': ['estoque'],
    'Nome': ['Paracetamol', 'Ibuprofeno', 'Amoxicilina', 'Loratadina', 'Omeprazol'],
    'Quantidade': [20, 15, 10, 25, 30],
    'Preco': [3.50, 5.00, 7.00, 2.50, 4.00],
}

carrinho = {
             'Titulo':['carrinho'],
             'Nome':[],
             'Quantidade':[],
             'Preco':[],
            }

arquivo_estoque = "estoque.json"
arquivo_carrinho = "carrinho.json"


def select_user():
    print("Bem vindo ao sistema de busca e encomenda de medicamentos!")
    user = int(input("Digite 1 para cliente ou 2 para funcionário: "))
    return user

def print_opcoes_cliente():
    print("1. Adicionar Item ao carrinho")
    print("2. Remover Item do carrinho")
    print("3. Exibir Resumo do Estoque")
    print("4. Exibir itens no carrinho")
    print("5. Confirmar encomenda")
    print("6. Sair\n")
    opcao = input("Escolha uma opção: ")
    return opcao

def print_opcoes_funcionario():
    print("1. Cadastrar ou adicionar item no estoque")
    print("2. Remover item do estoque")
    print("3. Exibir Resumo do Estoque")
    print("4. Editar valor de produto")
    print("5. Sair\n")
    opcao = input("Escolha uma opção: ")
    return opcao

def atualizar_carrinho(nome, remover, adicionar):
    if nome in remover['Nome']:
        while True:
            try:
                quantidade = int(input("Qual seria a quantidade? "))
                break
            except ValueError:
                print("Quantidade inválida. Por favor, digite um número inteiro!")
        if remover['Quantidade'] [remover['Nome'].index(nome)] >= quantidade:
            remover['Quantidade'] [remover['Nome'].index(nome)] -= quantidade
            adicionar_Item(nome, quantidade, adicionar)

        else:
            print("Quantidade indisponível")
            resumo_item(nome, remover)
    else:
        print("Item indisponível em estoque")  

def adicionar_Item(nome, quantidade, nome_estoque):
    if nome in nome_estoque['Nome']:
        nome_estoque['Quantidade'] [nome_estoque['Nome'].index(nome)] += quantidade  

    else:
        nome_estoque['Nome'].append(nome)
        nome_estoque['Quantidade'].append(quantidade)
        if nome_estoque == estoque:
            while True:
                try:
                    preco = float(input("Digite o preço do novo produto? "))
                    break
                except ValueError:
                    print("Preço inválido. Por favor, digite um número!")
            nome_estoque['Preco'].append(preco)

        elif nome_estoque == carrinho:
            nome_estoque['Preco'].append(estoque['Preco'] [estoque['Nome'].index(nome)])

            
            
    print(f"\nForam adicionadas {quantidade} unidades de {nome} ao {nome_estoque['Titulo'][0]}.")
    resumo_item(nome, nome_estoque)

def confirmar_compra():
    preco_total = 0
    for i in range(len(carrinho["Quantidade"])):
        preco_total += carrinho['Quantidade'][i] * carrinho["Preco"][i]
    print('Encomenda concluida com sucesso!\n')
    print('Resumo da compra:')
    for i in range(len(carrinho["Nome"])):
        print(f'{carrinho["Quantidade"][i]} unidades de {carrinho["Nome"][i]}')
    print(f'\nO valor total da compra é de R$: {preco_total}!')
    print('Obrigado por encomendar conosco!\n')     

def editar_preco():
    nome = input("Qual produto será alterado? ")
    
    if nome in estoque['Nome']:
        while True:
            try:
                preco = float(input("Digite o novo valor do produto: "))
                break
            except ValueError:
                    print("Preço inválido. Por favor, digite um número!")
        estoque['Preco'] [estoque['Nome'].index(nome)] = preco         

    else:
        print("Produto não encontrado. Por favor, digite um produto válido.")
        resumo_estoque(estoque)
        
def remover_item():
    nome = input("Qual item deseja excluir? ")
    if nome in estoque["Nome"]:
        quantidade = int(input("Digite a quantidade a ser removida: "))
        print()

        if estoque['Quantidade'] [estoque['Nome'].index(nome)] >= quantidade:
            estoque['Quantidade'] [estoque['Nome'].index(nome)] -= quantidade  
            print(f"{quantidade} unidades de {nome} removidas do estoque.")
            resumo_item(nome, estoque)
            with open(arquivo_estoque, "w") as arquivo:
                json.dump(estoque, arquivo, indent=4)
        else:
            print("Quantidade insuficiente em estoque.")
            resumo_estoque(estoque)

    else:
        print("Item não encontrado no estoque.")
        resumo_estoque(estoque)

def resumo_estoque(nome_estoque):
    print(f"\nResumo do {nome_estoque['Titulo'][0]}:")
    for nome, quantidade, preco in zip(nome_estoque["Nome"], nome_estoque["Quantidade"], nome_estoque["Preco"]):
        print(f"{nome}: {quantidade} unidades, R$:{preco}")
    print('')

def resumo_item(nome, nome_estoque):
    print(f"{nome_estoque['Quantidade'] [nome_estoque['Nome'].index(nome)]} unidades de {nome} em {nome_estoque['Titulo'][0]}\n ")
    
def home_cliente():
    while True:
        with open(arquivo_estoque, "w") as arquivo:
            json.dump(estoque, arquivo, indent=4)
        with open(arquivo_carrinho, "w") as arquivo:
            json.dump(carrinho, arquivo, indent=4)
            
        opcao = print_opcoes_cliente()
            
        if opcao == "1":
            nome = input("Qual item deseja comprar? ")
            atualizar_carrinho(nome, estoque, carrinho)
        elif opcao == "2":
            nome = input("Qual item deseja remover? ")
            atualizar_carrinho(nome, carrinho, estoque)
        elif opcao == "3":
            resumo_estoque(estoque)   
        elif opcao == "4":
            resumo_estoque(carrinho)
        elif opcao == "5":
            confirmar_compra()
            break
        elif opcao == "6":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

def home_funcionario():
    while True:
        with open(arquivo_estoque, "w") as arquivo:
            json.dump(estoque, arquivo, indent=4)
        with open(arquivo_carrinho, "w") as arquivo:
            json.dump(carrinho, arquivo, indent=4)
        
        opcao = print_opcoes_funcionario()
        
        if opcao == "1":
            nome = input("Qual item deseja adicionar? ")
            
            while True:
                try:
                    quantidade = int(input("Quantos itens serão adicionados? "))
                    break
                except ValueError:
                    print("Quantidade inválida. Por favor, digite um número inteiro!")

            adicionar_Item(nome, quantidade, estoque)
            
            
        elif opcao == "2":
            remover_item()
        elif opcao == "3":
            resumo_estoque(estoque)
        elif opcao == '4':
            editar_preco()
                
        elif opcao == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")     

def main():
    while True: 
        user = select_user()
        if user == 1:
            home_cliente()
            break
        elif user == 2:
            home_funcionario()
            break
        else:
            print("Opção inválida. Tente novamente.")
            
if __name__ == "__main__":
    main()

