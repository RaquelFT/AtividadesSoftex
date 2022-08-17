class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, novo_nome):
        self.__nome = novo_nome 

    @property
    def get_idade(self):
        return self.__idade 

nome_pessoa = Pessoa("Raquel", 31)
print(nome_pessoa.get_nome)
nome_pessoa.set_nome("aaaaa")
print(nome_pessoa.get_nome)
print(nome_pessoa.get_idade)

