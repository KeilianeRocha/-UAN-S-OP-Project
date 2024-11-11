# Script para calcular a porcentagem de resto-ingesta com base na quantidade produzida e consumida.


def calcular_resto_ingesta(quantidade_produzida, quantidade_consumida):
    if quantidade_produzida == 0:
        return "A quantidade produzida deve ser maior que zero."
    resto_ingesta = (
        (quantidade_produzida - quantidade_consumida) / quantidade_produzida
    ) * 100
    return f"Resto-Ingesta: {resto_ingesta:.2f}%"


# Exemplo de uso
quantidade_produzida = 100  # em kg
quantidade_consumida = 85  # em kg

print(calcular_resto_ingesta(quantidade_produzida, quantidade_consumida))
