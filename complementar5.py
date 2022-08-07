print("-------1-Soma-----------------")
print("-------2-Subtração------------")
print("-------3-Multiplicação--------")
print("-------4-Divisão--------------")
print("-------0-Sair-----------------")



def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        return num1 / num2


while True:
    opcao = int(input("Digite o número da operação que você deseja realizar\n"))
    if opcao == 0:
        break
    num1 = int(input("Digite o primeiro número\n"))
    num2 = int(input("Digite o segundo número\n"))
    print(calculadora(num1, num2, opcao))