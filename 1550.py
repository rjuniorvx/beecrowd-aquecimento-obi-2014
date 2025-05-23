from collections import deque  # Importa deque para usar como fila na BFS

T = int(input())  # Lê o número de casos de teste

for _ in range(T):
    A, B = map(int, input().split())  # Lê os valores de A e B

    fila = deque()  # Inicializa a fila para a busca em largura
    fila.append((A, 0))  # Adiciona o número inicial e o contador de passos
    visitado = set()  # Conjunto para guardar os números já visitados
    visitado.add(A)  # Marca o número inicial como visitado

    while fila:
        atual, passos = fila.popleft()  # Pega o próximo número e passos atuais

        if atual == B:
            print(passos)  # Se o número atual for o desejado, imprime os passos
            break  # Sai do loop para o próximo caso de teste

        # Operação 1: adicionar 1 ao número
        prox1 = atual + 1
        if prox1 <= 10000 and prox1 not in visitado:  # Verifica se ainda está no limite e não foi visitado
            visitado.add(prox1)  # Marca como visitado
            fila.append((prox1, passos + 1))  # Adiciona na fila com passos incrementados

        # Operação 2: inverter os dígitos do número
        prox2 = int(str(atual)[::-1])  # Inverte os dígitos e converte para inteiro
        if prox2 <= 10000 and prox2 not in visitado:  # Verifica os mesmos critérios
            visitado.add(prox2)  # Marca como visitado
            fila.append((prox2, passos + 1))  # Adiciona na fila
