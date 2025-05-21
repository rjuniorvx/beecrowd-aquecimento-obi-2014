import math  # Importa a biblioteca math para usar o valor de pi

C = int(input())  # Lê o número de casos de teste

for _ in range(C):  # Loop para cada caso de teste
    N, L = map(int, input().split())  # Lê o número de pessoas (N) e volume total de Coca-Cola em mL (L)
    b, B, H = map(int, input().split())  # Lê os valores de raio menor (b), maior (B) e altura total do copo (H)

    V_alvo = L / N  # Calcula o volume que cada pessoa deve receber (em cm³)

    # Inicializa a busca binária nos limites de altura do copo
    esquerda = 0.0  # Altura mínima
    direita = H     # Altura máxima (o copo inteiro)

    for _ in range(100):  # Realiza 100 iterações para garantir precisão
        h = (esquerda + direita) / 2  # Ponto médio da altura atual

        # Calcula o raio da parte superior do líquido em altura h (raio cresce linearmente com a altura)
        r_h = b + (B - b) * (h / H)

        # Calcula o volume do tronco de cone até a altura h
        volume = (1/3) * math.pi * h * (r_h**2 + r_h*b + b**2)

        # Verifica se o volume calculado é menor que o necessário
        if volume < V_alvo:
            esquerda = h  # Aumenta a altura mínima
        else:
            direita = h  # Diminui a altura máxima

    # Imprime a altura h com duas casas decimais
    print(f"{h:.2f}")
