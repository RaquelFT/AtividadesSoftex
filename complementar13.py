class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome 

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, aniversario = 1):
        self.__idade += aniversario

joao = Pessoa("Jão", 31)
print(joao.nome)
joao.nome = "Maria"
print(joao.nome)
print(joao.idade)
joao.idade = 2
print(joao.idade)

