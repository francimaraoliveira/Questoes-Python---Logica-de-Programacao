def converter_tempo():
    """
    Converte um número de segundos para horas, minutos e segundos.
    """
    while True:
        try:
            segundos = int(input("Digite um número em segundos: "))
            if segundos < 0:
                print("Por favor, digite um valor positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    
    horas = segundos // 3600  # Calcula o número de horas
    minutos = (segundos % 3600) // 60  # Calcula o número de minutos restantes
    segundos_restantes = segundos % 60  # Calcula os segundos restantes
    
    print(f"{segundos} segundos equivalem a {horas} horas, {minutos} minutos e {segundos_restantes} segundos.")

# Chamando a função
converter_tempo()