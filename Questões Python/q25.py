def verificar_elegibilidade_para_votar():
    """
    Verifica se uma pessoa é elegível para votar com base na idade.
    """
    print("Verifique sua elegibilidade para votar.")
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
                continue
            
            if idade >= 18:
                print("Você é elegível para votar.")
            elif 16 <= idade < 18:
                print("Você é elegível para votar, mas o voto é opcional.")
            else:
                print("Você ainda não é elegível para votar.")
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# Chamando a função
verificar_elegibilidade_para_votar()