import os
os.system('clear')


quantidade_morangos = float(input("Digite a quantidade de morangos (em Kg): "))
quantidade_macas = float(input("Digite a quantidade de maçãs (em Kg): "))


if quantidade_morangos <= 5:
    preco_morangos = quantidade_morangos * 2.50
else:
    preco_morangos = quantidade_morangos * 2.20

if quantidade_macas <= 5:
     preco_macas = quantidade_macas * 1.80
else:
    preco_macas = quantidade_macas * 1.50
total_kg = quantidade_morangos + quantidade_macas
total_compra = preco_morangos + preco_macas

if total_kg >= 10 or total_compra > 15.00:
    total_compra *= 0.90


print(f"O valor total a ser pago é: R$ {total_compra:.2f}")








