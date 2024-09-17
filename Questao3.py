# não encontrei o arquivo json, então criei um com 30 valores de faturamento

import json

data = '''
[
    {
        "faturamento": [
            "22334,00",
            "44565,00",
            "21677,43",
            "33654,55",
            "33633,99",
            "21456,76",
            "51765,00",
            "33764,30",
            "42765,65",
            "47800,50",
            "38800,78",
            "21546,66",
            "24768,00",
            "50788,44",
            "21764,87",
            "27086,32",
            "35500,99",
            "46100,78",
            "50077,00",
            "51500,99",
            "45788,66",
            "34788,00",
            "56700,88",
            "31900,88",
            "29899,00",
            "29900,88",
            "31898,99",
            "39800,00",
            "38000,77"
        ]
    }
]
'''


faturamento = json.loads(data)
valores = faturamento[0]["faturamento"]

valores_float = [float(valor.replace(',', '.')) for valor in valores]

maior_valor = max(valores_float)
menor_valor = min(valores_float)
media_valores= sum(valores_float)/len(valores_float)
print("o maior valor de faturamento foi: ",maior_valor," , o menor valor de faturamento foi: ", menor_valor, " e a média do faturamento mensal foi de: ", media_valores)
  