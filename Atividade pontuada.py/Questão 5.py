import os
os.system('clear')


operacao = input("Digite o código de operação (+, -, *, /): ")

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))


match operacao:
    case "+":
        resultado = A + B
        print("O resultado da operação é:", resultado)
    case "-":
        resultado = A - B
        print("O resultado da operação é:", resultado)
    case "*":
        resultado = A * B
        print("O resultado da operação é:", resultado)
    case "/":
        if B != 0:
            resultado = A / B
            print("O resultado da operação é:", resultado)
        else:
            print("Erro: Divisão por zero!")
    case _:
        print("Erro: Operação inválida!")

























              