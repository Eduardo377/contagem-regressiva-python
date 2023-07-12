import time

def contagem_regressiva(segundos):
    print("Inicializando contagem regresiva")

    for i in range(segundos, 0, -1):
        print(str(i))
        time.sleep(1) # Aguarda 1 segundo antes de imprimir o próximo número
        segundos -= 1
    print("BUM")

# Exemplo de uso: contagem regressiva de 10 segundos
contagem_regressiva(10)