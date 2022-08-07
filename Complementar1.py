nome_aluno = input("Escreva seu nome: ")
nota_1 = int(input("Escreva a primeira nota: "))
nota_2 = int(input("Escreva a segunda nota: "))
media = (nota_1 + nota_2)/2
num_faltas = int(input("Escreva o número de faltas: "))

if media < 7 or num_faltas > 3:
    print(nome_aluno + " reprovado")
else:
    print(nome_aluno + " aprovado")

