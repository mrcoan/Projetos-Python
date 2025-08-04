# Analisador de números avançado --------------------------------------------------------

numeros = []
numeros_pares = []
numeros_impares = []
numeros_positivos = []
numeros_negativos = []

def numero_par_impar():
    for numero in numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)
        else:
            numeros_impares.append(numero)

def numero_positivo_negativo():
    for numero in numeros:
        if numero > 0:
            numeros_positivos.append(numero)
        else:
            numeros_negativos.append(numero)

print("\nBem-vindo ao Analisador de números avançado!")
while True:
    try:
        numero = int(input("Digite um número inteiro (0 para sair): "))
    except ValueError:
        print("Digite um número válido.")
    else:
        if numero == 0:
            print("Finalizando...")
            break
        else:
            numeros.append(numero)
            print("Número adicionado com sucesso.")

if len(numeros) != 0:
    print("\nDados:")
    print(f"Números digitados: {numeros}.")
    
    media = sum(numeros) / len(numeros)
    print(f"Média dos números: {media}.")
    
    maior = max(numeros)
    print(f"Maior número digitado: {maior}.")
    
    menor = min(numeros)
    print(f"Menor número digitado: {menor}.")
    
    numero_par_impar()
    numero_positivo_negativo()
    
    print(f"Números pares: {numeros_pares}.")
    print(f"Números ímpares: {numeros_impares}.")
    print(f"Números positivos: {numeros_positivos}.")
    print(f"Números negativos: {numeros_negativos}.")
    
    top3 = sorted(numeros, reverse=True)[:3]
    print(f"Top 3 maiores números: {top3}.")
else:
    print("Nenhum numero foi adicionado.")