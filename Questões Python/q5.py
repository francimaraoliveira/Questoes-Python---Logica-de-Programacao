def ler_numeros():
    """
    Ler vários números ao usuário e só para de ler os números quando o usuário digitar "0".
    """
    print("Digite números (digite 0 para sair):")
    numeros = []  # Lista para armazenar os números
    while True:
        try:
            numero = int(input("Digite um número: "))
            if numero == 0:  # Condição de parada
                break
            numeros.append(numero)
        except ValueError:
            print("Por favor, digite um número válido.")
    print(f"Números digitados: {numeros}")

# Chamando a função
ler_numeros()