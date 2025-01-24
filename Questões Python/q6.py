def calcular_soma():
    """
    Solicita ao usuário que digite 15 números e calcula a soma deles.
    """
    print("Digite 15 números:")
    soma = 0
    
    for i in range(1, 16):  # Loop para ler 15 números
        while True:
            try:
                numero = float(input(f"Digite o {i}º número: "))
                soma += numero
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número válido.")
    
    print(f"A soma dos 15 números digitados é: {soma}")

# Chamando a função 
calcular_soma()