def verificar_ano_bissexto():
    """
    Verifica se um ano informado pelo usuário é bissexto.
    """
    while True:
        try:
            ano = int(input("Digite um ano para verificar se é bissexto: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    # Um ano é bissexto se for divisível por 4 e (não divisível por 100 ou divisível por 400)
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")

# Chamando a função
verificar_ano_bissexto()