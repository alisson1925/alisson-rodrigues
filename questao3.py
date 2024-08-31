import json
import os

def calcular_faturamento(file_path):
    if not os.path.exists(file_path):
        return {"erro": "Arquivo não encontrado."}

    with open(file_path, 'r') as file:
        dados = json.load(file)['faturamento_diario']

    valores = [v for v in dados.values() if v > 0]
    if not valores:
        return {"erro": "Não há faturamento."}

    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)
    dias_acima_media = sum(v > media for v in valores)

    return {
        "menor_faturamento": menor,
        "maior_faturamento": maior,
        "dias_acima_media": dias_acima_media
    }

# Arquivo fauramento.json aqui
file_path = 'faturamento.json'
resultado = calcular_faturamento(file_path)

if "erro" in resultado:
    print(resultado["erro"])
else:
    print(f"Menor Faturamento: R${resultado['menor_faturamento']:.2f}")
    print(f"Maior Faturamento: R${resultado['maior_faturamento']:.2f}")
    print(f"Número de dias acima da média: {resultado['dias_acima_media']}")
