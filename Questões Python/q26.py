def verificar_triangulo():
    """
    Verifica se três valores podem formar os lados de um triângulo.
    """
    print("Verifique se três valores podem formar um triângulo.")
    try:
        # Solicita os três lados ao usuário
        lado1 = float(input("Digite o valor do primeiro lado: "))
        lado2 = float(input("Digite o valor do segundo lado: "))
        lado3 = float(input("Digite o valor do terceiro lado: "))

        # Verifica se os valores podem formar um triângulo usando a desigualdade triangular
        if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
            print("Os valores podem formar um triângulo.")
        else:
            print("Os valores NÃO podem formar um triângulo.")
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")

# Chamando a função
verificar_triangulo()