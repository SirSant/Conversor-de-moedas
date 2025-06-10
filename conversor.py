# Conversor de Moedas - v1

# Entrada do valor em reais
valor_brl = float(input("Digite o valor em Reais (BRL): "))

# Escolha da moeda de destino
print("Escolha a moeda para conversão:")
print("1 - Dólar (USD)")
print("2 - Euro (EUR)")
print("3 - Libra (GBP)")
opcao = input("Digite o número da moeda desejada: ")

import requests

def obter_taxa(moeda_destino):
    url = f"https://economia.awesomeapi.com.br/last/BRL-{moeda_destino}"
    resposta = requests.get(url)
    if resposta.status_code != 200:
        raise Exception("Erro ao acessar a API da AwesomeAPI.")
    dados = resposta.json()
    chave = f"BRL{moeda_destino}"
    if chave not in dados or 'bid' not in dados[chave]:
        raise Exception("Erro: resposta da API não contém a taxa de câmbio.")
    return float(dados[chave]['bid'])

while True:
    print("Escolha a moeda para conversão:")
    print("1 - Dólar (USD)")
    print("2 - Euro (EUR)")
    print("3 - Libra (GBP)")
    print("0 - Sair")
    escolha = input("Digite o número da moeda desejada: ")

    if escolha == '0':
        print("Encerrando o programa.")
        break

    moedas = {'1': 'USD', '2': 'EUR', '3': 'GBP'}

    if escolha in moedas:
        try:
            valor_brl = float(input("Digite o valor em Reais (BRL): "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue
        moeda_destino = moedas[escolha]
        print(f"Consultando taxa de câmbio BRL → {moeda_destino}...")
        try:
            taxa = obter_taxa(moeda_destino)
            convertido = valor_brl * taxa
            print(f"Valor em {moeda_destino}: {convertido:.2f}")
        except Exception as e:
            print("Erro:", e)
    else:
        print("Opção inválida.")