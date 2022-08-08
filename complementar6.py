nome = input("Escreva seu nome completo\n")
ano_nascimento = input("Escreva seu ano de nascimento\n")
idade = 0
while True:
    if ano_nascimento.isdigit():
        if int(ano_nascimento) >=1922 and int(ano_nascimento) <=2021:
            idade = 2022 - int(ano_nascimento)
            break
    print("Entrada inválida")
    ano_nascimento = input("Escreva seu ano de nascimento\n")         
print("A idade que você completou ou completará em 2022 é " + str(idade) + " anos")    

