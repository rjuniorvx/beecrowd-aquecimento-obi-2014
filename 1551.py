# Lê o número de casos de teste
n = int(input())

# Loop para processar cada caso de teste
for _ in range(n):
    # Lê a frase e converte para letras minúsculas
    frase = input().lower()

    # Cria um conjunto para armazenar as letras únicas da frase
    letras = set()

    # Percorre cada caractere da frase
    for c in frase:
        # Verifica se o caractere é uma letra entre 'a' e 'z'
        if 'a' <= c <= 'z':
            # Adiciona a letra ao conjunto
            letras.add(c)

    # Conta quantas letras únicas foram encontradas
    total = len(letras)

    # Se tem todas as 26 letras do alfabeto
    if total == 26:
        print("frase completa")
    # Se tem pelo menos 13 letras diferentes
    elif total >= 13:
        print("frase quase completa")
    # Se tem menos de 13 letras diferentes
    else:
        print("frase mal elaborada")
