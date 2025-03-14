import os
os.system('clear')


renda_mensal = float(input("Digite a renda mensal do solicitante: R$ "))
valor_emprestimo = float(input("Digite o valor total do empréstimo solicitado: R$ "))
numero_prestacoes = int(input("Digite o número de prestações que o solicitante deseja pagar: "))
valor_prestacao = valor_emprestimo / numero_prestacoes


if valor_emprestimo <= 10 * renda_mensal and valor_prestacao <= 0.3 * renda_mensal:
    print("O empréstimo pode ser concedido!")
else:
    print("O empréstimo não pode ser concedido!")