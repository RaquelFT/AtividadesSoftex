class Carro:
    total_de_carros = 0
    @staticmethod
    def cont_carro():
        Carro.total_de_carros += 1


carro1 = Carro()
carro2 = Carro()
carro3 = Carro()
Carro.cont_carro()
Carro.cont_carro()
Carro.cont_carro()
print(Carro.total_de_carros)