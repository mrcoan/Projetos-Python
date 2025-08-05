# Organizador de Tarefas (To-do list) --------------------------------------------------------

tarefas = []
tarefas_finalizadas = []

def adicionar_tarefa():
    print("\nAdicionar Tarefa:")
    tarefa = input("Digite a tarefa para adicionar: ").strip().lower()
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa.capitalize()}' adicionada a lista.")

def tarefas_pendentes():
    if len(tarefas):
        print("\nTarefas pendentes:")
        for indice, tarefa in enumerate(tarefas, start=1):
            print(f"Tarefa {indice}: {tarefa.capitalize()}")
        print(f"{len(tarefas)} tarefa(s) pendente(s).")
    else:
        print("Não há tarefas pendentes.")

def concluir_tarefa():
    if len(tarefas):
        try:
            print("\nConcluir Tarefas: ")
            numero = int(input("Digite o número da tarefa que foi concluída: "))
            if numero < 1 or numero > len(tarefas):
                raise ValueError
            else:
                tarefa_concluida = tarefas.pop(numero-1)
                print(f"Tarefa '{tarefa_concluida.capitalize()}' concluída com sucesso.")
                tarefas_finalizadas.append(tarefa_concluida)
        except ValueError:
            print("Digite um número válido.")
    else:
        print("Não há tarefas para concluir.")

def tarefas_concluidas():
    if len(tarefas_finalizadas):
        print("\nTarefas concluídas: ")
        for indice, tarefa in enumerate(tarefas_finalizadas, start=1):
            print(f"Tarefa {indice}: {tarefa.capitalize()}.")
        
        print(f"{len(tarefas_finalizadas)} tarefa(s) concluída(s).")
    else:
        print("Não há tarefas finalizadas.")

print("Organizador de Tarefas (To-do list)")

while True:
    print("\nMenu de tarefas: 0=sair / 1= adicionar tarefa / 2= visualizar tarefas pendentes / 3= concluir tarefa / 4= tarefas concluídas.")
    try:
        menu = int(input("escolha uma das opções: "))
        if menu < 0 or menu > 4:
            raise ValueError
    except ValueError:
        print("Digite uma opção válida.")
    else:
        match menu:
            case 0:
                print("Encerrando o programa...")
                break
            case 1:
                adicionar_tarefa()
            case 2:
                tarefas_pendentes()
            case 3:
                concluir_tarefa()
            case 4:
                tarefas_concluidas()

print("\nObrigado por utilizar o Organizador de tarefas. Até logo!")
