# Agenda de Contatos --------------------------------------------------------

contatos ={}

def cadastrar_contato(nome, telefone):
    contatos[nome] = telefone
    print(f"{nome} cadastrado com sucesso.")

def buscar_contato(nome):
    if nome in contatos:
        print("\nContato encontrado:")
        print(f"{nome.title()}, {telefone}.")
    else:
        print("Contato não encontrado.")

def remover_contato(nome):
    if nome in contatos:
        del contatos[nome]
        print(f"Contato {nome.title()} excluído com sucesso.")
    else:
        print("Contato não encontrado.")

print("\nAgenda de Contatos:")

while True:
    print("\nOpções: 0= sair / 1= cadastrar contato / 2= buscar contato / 3= remover contato / 4= listagem completa")
    try:
        menu = int(input("Digite uma opção: "))
        if menu < 0 or menu > 4:
            raise ValueError
    except ValueError:
        print("Digite uma opção válida.")
    else:
        match menu:

            case 0:
                print("\nFinalizando programa...")
                break

            case 1:
                print("\nCadastro de novo contato:")
                nome = input("Digite o nome: ").strip().lower()
                telefone = input("Digite o telefone: ").strip()
                cadastrar_contato(nome, telefone)

            case 2:
                print("\nBuscar contato:")
                if len(contatos):
                    nome = input("Digite o nome: ").strip().lower()
                    buscar_contato(nome)
                else:
                    print("Nao há contatos na agenda.")
            
            case 3:
                print('\nRemover contato:')
                if len(contatos):
                    nome = input("Digite o nome: ").strip().lower()
                    remover_contato(nome)
                else:
                    print("Nao há contatos na agenda.")

            case 4:
                print("\Contatos registrados:")
                if len(contatos):
                    for contato, telefone in sorted(contatos.items()):
                        print(f"{contato.title()}, {telefone}.")
                else:
                    print("Não há contatos na agenda.")
