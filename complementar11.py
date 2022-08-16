class NumComplexos:
    def __init__(self, num_real, num_imaginario):
        self.num_real = num_real
        self.num_imaginario = num_imaginario

    def __str__(self):
        return str(self.num_real)+"+"+str(self.num_imaginario)+"j" 
    
    def soma_complexo(self, complex_2, complex_3=0):
        soma_real = sum([self.num_real, complex_2.num_real, complex_3.num_real])
        soma_imag = sum([self.num_imaginario, complex_2.num_imaginario, complex_3.num_imaginario])
        return str(soma_real)+"+"+str(soma_imag)+"j" 

    def subtracao_complexo(self, complex_2, complex_3=0):
        subtracao_real = sum([self.num_real, -complex_2.num_real, -complex_3.num_real])
        subtracao_imag = sum([self.num_imaginario, -complex_2.num_imaginario, -complex_3.num_imaginario])
        if subtracao_real >= 0 and subtracao_imag >=0:
            return str(subtracao_real)+"+"+str(subtracao_imag)+"j"
        return str(subtracao_real)+str(subtracao_imag)+"j"

    def multiplicacao_complexo(self, complex_2, complex_3=0):
        multiplicacao_real = self.num_real * complex_2.num_real * complex_3.num_real
        multiplicacao_imag = self.num_imaginario * complex_2.num_imaginario * complex_3.num_imaginario
        if multiplicacao_real >= 0 and multiplicacao_imag >=0:
            return str(multiplicacao_real)+"+"+str(multiplicacao_imag)+"j"
        return str(multiplicacao_real)+str(multiplicacao_imag)+"j"    

    def divisao_complexo(self, complex_2, complex_3=0):
        divisao_real = self.num_real / complex_2.num_real / complex_3.num_real
        divisao_imag = self.num_imaginario / complex_2.num_imaginario / complex_3.num_imaginario
        if divisao_real >= 0 and divisao_imag >=0:
            return str(divisao_real)+"+"+str(divisao_imag)+"j"
        return str(divisao_real)+str(divisao_imag)+"j"    


a = NumComplexos(5, 9)
b = NumComplexos(2, 7)
c = NumComplexos(2, 3)


print(a.soma_complexo(b, c))
print(a.subtracao_complexo(b, c))
print(a.multiplicacao_complexo(b, c))
print(a.divisao_complexo(b, c))
