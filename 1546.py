# Lê o número de casos de teste (dias de trabalho)
n = int(input())

# Dicionário que associa cada tipo de feedback ao responsável
responsaveis = {
    1: "Rolien",    # 1 = Elogios
    2: "Naej",      # 2 = Bugs
    3: "Elehcim",   # 3 = Dúvidas
    4: "Odranoel"   # 4 = Sugestões
}

# Loop externo para percorrer cada caso de teste (cada dia de trabalho)
for _ in range(n):
    # Lê o número de feedbacks recebidos no dia atual
    k = int(input())
    
    # Loop interno para processar cada feedback do dia
    for _ in range(k):
        # Lê o tipo do feedback (1 a 4)
        tipo = int(input())
        
        # Imprime o nome do responsável correspondente ao tipo de feedback
        print(responsaveis[tipo])
