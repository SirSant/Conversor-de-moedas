# Conversor de Moedas - v1

# Entrada do valor em reais
valor_brl = float(input("Digite o valor em Reais (BRL): "))

# Escolha da moeda de destino
print("Escolha a moeda para conversão:")
print("1 - Dólar (USD)")
print("2 - Euro (EUR)")
print("3 - Libra (GBP)")
opcao = input("Digite o número da moeda desejada: ")

# Taxas de câmbio fixas (valores do dia 04/06/2025)

taxa_usd = 5.20 # 1 USD = 5.20 BRL
taxa_eur = 5.60 # 1 EUR = 5.60 BRL
taxa_gbp = 6.10 # 1 GBP = 6.10 BRL

#Conversão
if opcao == "1":
    valor_convertido = valor_brl / taxa_usd
    print(f"Valor em Dólares (USD): ${valor_convertido:.2f}")
elif opcao == "2":
    valor_convertido = valor_brl / taxa_eur
    print(f"Valor em Euros (EUR): €{valor_convertido:.2f}")
elif opcao == "3":
    valor_convertido = valor_brl / taxa_gbp
    print(f"Valor em Libras (GBP): £{valor_convertido:.2f}")
else:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")