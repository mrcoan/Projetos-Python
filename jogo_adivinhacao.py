import random

# jogo de adivinhação --------------------------------------------------------

numero_correto = random.randint(1, 10)

print("Bem-vindo(a) ao jogo de adivinhação!")
print("A máquina irá gerar um número entre 1 e 10, e seu objetivo é tentar acertar.")
print("Você tem 3 vidas.")

vida = 3

while True:
    try:
        numero_jogador = int(input("Digite um numero (0 para sair): "))
        if numero_jogador > 10 or numero_jogador < 0:
            raise ValueError
    except ValueError:
        print("Digite um número válido entre 1 e 10.")
    else:
        if numero_jogador == 0:
            print("Encerrando...")
            break
        
        elif numero_jogador == numero_correto:
            print("Você acertou!")
            print(f"O número escolhido pela máquina foi {numero_correto}.")
            break
        
        else:
            vida -= 1
            if numero_jogador > numero_correto:
                print("Número alto, tente novamente.")
            else:
                print("Número baixo, tente novamente.")
            
            if vida > 0:
                print(f"Vidas restantes: {vida}.")
            else:
                print("Suas vidas acabaram.")
                print(f"O número escolhido pela máquina foi {numero_correto}.")
                break