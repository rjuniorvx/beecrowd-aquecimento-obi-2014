# Lê a quantidade de casos de teste (camisetas a serem sorteadas)
i = int(input())

# Loop para processar cada caso de teste
for _ in range(i):
    # Lê a quantidade de alunos no grupo (QT) e o número secreto (S)
    entrada = input().split()
    QT = int(entrada[0])
    S = int(entrada[1])

    # Lê os palpites dos alunos e converte para uma lista de inteiros
    palpites = list(map(int, input().split()))

    # Inicializa o vencedor com 0 (posição inválida) e a menor diferença com um valor alto
    vencedor = 0
    menor_diferenca = 101  # maior que qualquer diferença possível (1 a 100)

    # Percorre os palpites dos alunos
    for i in range(QT):
        # Se o palpite for exatamente igual ao número secreto
        if palpites[i] == S:
            vencedor = i + 1  # Ganhador é o primeiro a acertar (posição começa em 1)
            break  # Encerra o loop, pois já há um ganhador exato
        else:
            # Calcula a diferença absoluta entre o palpite e o número secreto
            diferenca = abs(palpites[i] - S)
            # Se ainda não há ganhador ou a diferença atual é menor que a menor já encontrada
            if vencedor == 0 or diferenca < menor_diferenca:
                menor_diferenca = diferenca  # Atualiza a menor diferença
                vencedor = i + 1  # Atualiza o possível ganhador (mais próximo do número secreto)

    # Imprime a posição do ganhador para o caso atual
    print(vencedor)
