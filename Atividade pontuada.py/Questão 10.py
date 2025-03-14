import os 
os.system('clear')


def calcular_valor(litros, tipo_combustivel):
    preco_gasolina = 6.59
    preco_alcool = 3.79
    
    if tipo_combustivel == 'G':  # Gasolina
        if litros <= 25:
            desconto = 0.03  # 3% de desconto
        else:
            desconto = 0.05  # 5% de desconto
        preco_por_litro = preco_gasolina
    elif tipo_combustivel == 'A':  # Álcool
        if litros <= 25:
            desconto = 0.02  # 2% de desconto
        else:
            desconto = 0.04  # 4% de desconto
        preco_por_litro = preco_alcool
    else:
        return "Tipo de combustível inválido!"

    
    valor_bruto = litros * preco_por_litro
    desconto_total = valor_bruto * desconto
    valor_final = valor_bruto - desconto_total

    return round(valor_final, 2)



litros_vendidos = float(input("Digite o número de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A para álcool, G para gasolina): ").upper()


valor_a_pagar = calcular_valor(litros_vendidos, tipo_combustivel)

print(f"O valor a ser pago pelo cliente é: R$ {valor_a_pagar}")
