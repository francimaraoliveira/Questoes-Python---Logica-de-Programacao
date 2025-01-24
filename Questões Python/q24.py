def calcular_media_ponderada():
    """
    Calcula a média ponderada de três números com seus respectivos pesos.
    """
    print("Digite três números e seus respectivos pesos.")
    
    numeros = []
    pesos = []
    
    # Loop para entrada dos números e pesos
    for i in range(1, 4):
        while True:
            try:
                numero = float(input(f"Digite o {i}º número: "))
                peso = float(input(f"Digite o peso do {i}º número: "))
                if peso <= 0:
                    print("O peso deve ser maior que zero. Tente novamente.")
                    continue
                numeros.append(numero)
                pesos.append(peso)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira valores numéricos.")
    
    # Calcula a média ponderada
    soma_ponderada = sum(n * p for n, p in zip(numeros, pesos))
    soma_pesos = sum(pesos)
    media_ponderada = soma_ponderada / soma_pesos
    
    print(f"A média ponderada dos números é: {media_ponderada:.2f}")

# Chamando a função
calcular_media_ponderada()