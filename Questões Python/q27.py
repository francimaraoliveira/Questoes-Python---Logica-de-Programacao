def calcular_media_aluno():
    """
    Calcula a média de um aluno com base em 4 notas e verifica se ele foi aprovado,
    reprovado ou se tem direito à recuperação.
    """
    print("Sistema de cálculo de média escolar")
    
    # Entrada das 4 notas do aluno
    notas = []
    for i in range(1, 5):
        while True:
            try:
                nota = float(input(f"Digite a {i}ª nota do aluno: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida! Digite um valor entre 0 e 10.")
            except ValueError:
                print("Entrada inválida! Digite um número válido.")
    
    # Calcula a média
    media = sum(notas) / 4
    print(f"\nMédia das 4 notas: {media:.2f}")
    
    # Verifica a situação do aluno
    if media >= 7:
        print("Aluno APROVADO!")
    else:
        print("Aluno em RECUPERAÇÃO. Precisa fazer uma prova.")
        while True:
            try:
                nota_recuperacao = float(input("Digite a nota da recuperação: "))
                if 0 <= nota_recuperacao <= 10:
                    break
                else:
                    print("Nota inválida! Digite um valor entre 0 e 10.")
            except ValueError:
                print("Entrada inválida! Digite um número válido.")
        
        # Verifica se o aluno foi aprovado na recuperação
        if nota_recuperacao >= 6:
            print("Aluno APROVADO na recuperação!")
        else:
            print("Aluno REPROVADO.")

# Chamando a função
calcular_media_aluno()