import os
os.system('clear')


tabela_precos = {
    "Verde": 10.00,
    "Azul": 20.00,
    "Amarelo": 30.00,
    "Vermelho": 40.00
}

cor = input("Digite a cor do CD: ").capitalize()


if cor in tabela_precos:
    print(f"O preço do CD {cor} é: R$ {tabela_precos[cor]:.2f}")
else:
    print("Cor inválida!")