print("-------1-Soma-----------------")
print("-------2-Subtração------------")
print("-------3-Multiplicação--------")
print("-------4-Divisão--------------")
opcao = int(input("Digite o número da operação que você deseja realizar\n"))
num1 = int(input("Digite o primeiro número\n"))
num2 = int(input("Digite o segundo número\n"))


def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        return num1 / num2
    return 0

print(calculadora(num1, num2, opcao))
