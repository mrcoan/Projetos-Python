# Simulador de Loja --------------------------------------------------------

estoque = {
    "notebook": 3500.00,
    "smartphone": 2400.00,
    "fones de ouvido": 150.00,
    "mochila": 180.00,
    "monitor": 899.90,
    "mouse": 99.90,
    "teclado": 120.00
}

carrinho = {}

def adicionar_produto(produto):
    if produto in estoque:
        valor = estoque[produto]
        carrinho[produto] = valor
        print(f"{produto.capitalize()} adicionado ao carrinho.")
    else:
        print("Produto não encontrado.")

def remover_produto(produto):
    if produto in carrinho:
        del carrinho[produto]
        print(f"{produto.capitalize()} removido do carrinho.")
    else:
        print("Produto não encontrado.")

print("Loja de Informática")

while True:
    print("\nopções: 0= sair / 1= visualizar produtos / 2= adicionar produto/ 3= visualizar carrinho / 4= remover produto")
    try:
        menu = int(input("Digite uma opção: "))
        if menu < 0 or menu > 4:
            raise ValueError
    except ValueError:
        print("Digite uma opção válida.")
    else:    
        match menu:
            case 0:
                print("\nFinalizando...")
                break
        
            case 1:
                print("\nProdutos no estoque:")
                for produto, valor in estoque.items():
                    print(f"{produto.capitalize()}, R${valor}.")
            
            case 2:
                print("\nAdicionar um produto ao carrinho:")
                produto = input("Nome do produto: ").lower().strip()
                adicionar_produto(produto)
            
            case 3:
                soma = 0
                print("\nCarrinho:")
                if carrinho:
                    for produto, valor in carrinho.items():
                        print(f"{produto.capitalize()}, R${valor}.")
                        soma += valor
                    print(f"Valor total: {soma:.2f}")
                else:
                    print("Não há produtos no carrinho.")
            
            case 4:
                print("\nRemover um produto do carrinho:")
                produto = input("Nome do produto: ").lower().strip()
                remover_produto(produto)