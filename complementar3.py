import time
contador_bomba = 10
print("Iniciando contagem regressiva")
while contador_bomba > 0:
    print(contador_bomba) 
    time.sleep(1)
    contador_bomba -= 1
print("BUM!")    