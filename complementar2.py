qtd_rodas = int(input("Escreva o número de rodas do veículo: "))
peso_bruto = float(input("Escreva o peso bruto do seu veículo em kg: "))
qtd_pessoas_no_veiculo = int(input("Escreva a quantidade de pessoas no veículo: "))

if qtd_rodas >= 2 and qtd_rodas <=3:
    print("A categoria da habilitação é A.")
elif qtd_rodas == 4 and qtd_pessoas_no_veiculo <= 8 and peso_bruto <=3500:
    print("A categoria da habilitação é B.")
elif qtd_rodas >=4 and peso_bruto >=3500 and peso_bruto <= 6000:
    print("A categoria da habilitação é C.")
elif qtd_rodas >= 4 and qtd_pessoas_no_veiculo >= 8:
    print("A categoria da habilitação é D.")
elif qtd_rodas >= 4 and peso_bruto >= 6000:
    print("A categoria da habilitação é E.")               
