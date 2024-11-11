# Script para calcular a quantidade de insumos necessária considerando FIFO, fatores de cocção, correção, e per capita.

# Exemplo de dados
estoque = {
    "batata": {"quantidade": 100, "validade": "2024-09-10"},
    "cenoura": {"quantidade": 50, "validade": "2024-09-15"},
}

# Fatores de Cocção e Correção
fatores = {
    "batata": {"fator_coccao": 0.8, "fator_correcao": 0.9},
    "cenoura": {"fator_coccao": 0.7, "fator_correcao": 0.85},
}

# Função para calcular quantidade final usando fatores
def calcular_quantidade_final(insumo, quantidade_bruta):
    fator_coccao = fatores[insumo]["fator_coccao"]
    fator_correcao = fatores[insumo]["fator_correcao"]
    return quantidade_bruta * fator_coccao * fator_correcao

# Função de controle FIFO
def utilizar_fifo(estoque):
    sorted_estoque = sorted(estoque.items(), key=lambda x: x[1]["validade"])
    return sorted_estoque[0]

# Exemplo de uso
insumo_selecionado = utilizar_fifo(estoque)
quantidade_final = calcular_quantidade_final(insumo_selecionado[0], insumo_selecionado[1]["quantidade"])

print(f"Insumo a ser utilizado: {insumo_selecionado[0]}")
print(f"Quantidade final utilizável: {quantidade_final} kg")
