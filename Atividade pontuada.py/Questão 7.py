import os 
os.system('clear')

nome_produto = input("Digite a descrição do produto(nome): ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário: "))

total = quantidade*preco_unitario
if quantidade <= 5:
    desconto_percentual = 2
elif quantidade <=10:
    desconto_percentual = 3
else:
    desconto_percentual = 5

desconto = total *(desconto_percentual/100)
total_a_pagar = total - desconto

print(f"nDescrição do produto:{nome_produto}")
print(f"Quantidade adquirida:{quantidade}")
print(f"Preço unitário:R${preco_unitario:.2f}")
print(f"Valor total:R${total:.2f}")
print(f"Desconto aplicado({desconto_percentual}%):R${desconto:.2f}")
print(f"Total a pagar:R${total_a_pagar:.2f}")