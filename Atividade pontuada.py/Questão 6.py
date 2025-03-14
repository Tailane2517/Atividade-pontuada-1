import os
os.system('clear')

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

média = (nota1 + nota2) /2
print(f"\nA média do aluno é:{média:.2f}")

if média >= 6.0:
    print("Parabéns!Você esta aprovado! ")
elif média >= 4.0:
    print("Você está de recuperação.")
else:
    print("Infelizmente, você está reprovado.")
