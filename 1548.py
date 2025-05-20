# Leitura do número de casos de teste
n = int(input())

# Para cada caso de teste
for _ in range(n):
    # Leitura do número de alunos
    m = int(input())

    # Leitura das notas dos alunos na ordem de chegada
    original = [int(x) for x in input().split(' ')]

    # Criação da lista ordenada das notas em ordem decrescente
    ordenado = sorted(original, reverse=True)

    # Inicializa o contador de alunos que não mudaram de lugar
    resposta = 0
    for i in range(m):
        # Compara se a nota na posição original é igual à da posição na fila ordenada
        if (original[i] == ordenado[i]):
            resposta += 1  # Conta se o aluno permaneceu na mesma posição

    # Imprime o total de alunos que não mudaram de lugar
    print(resposta)