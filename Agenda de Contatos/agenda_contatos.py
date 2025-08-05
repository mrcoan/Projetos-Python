# Agenda de Contatos --------------------------------------------------------

contatos ={}

def cadastrar_contato(nome, telefone, email):
    if nome in contatos:
        print("\nNome já cadastrado.")
        while True:
            try:
                alterar = int(input("Deseja atualizar os dados já cadastrados (1= sim / 2= não)? "))
                if alterar < 1 or alterar > 2:
                    raise ValueError

                if alterar == 1:
                    contatos[nome] = {"telefone": telefone, "email": email}
                    print(f"Contato {nome.title()} atualizado com sucesso.")
                else:
                    print(f"Dados não alterados no contato {nome.title()}")
                break
            except ValueError:
                print("Digite uma opção válida.")
    else:
        contatos[nome] = {"telefone": telefone, "email": email}
        print(f"{nome.title()} cadastrado(a) com sucesso.")

def buscar_contato(nome):
    if nome in contatos:
        informacao_contato = contatos[nome]  # Correção aqui
        print("\nContato encontrado:")
        print(f"{nome.title()}, {informacao_contato['telefone']}, {informacao_contato['email']}.")
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
                nome = input("Nome: ").strip().lower()
                telefone = input("Telefone: ").strip()
                email = input("E-mail: ").strip().lower()
                cadastrar_contato(nome, telefone, email)

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
                print("\nContato(s) registrado(s):")
                if len(contatos):
                    for contato, informacao_contato in sorted(contatos.items()):
                        print(f"{contato.title()}, {informacao_contato['telefone']}, {informacao_contato['email']}.")
                    print(f"{len(contatos)} contatos registrados.")
                else:
                    print("Não há contatos na agenda.")
