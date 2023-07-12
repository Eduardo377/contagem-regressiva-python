import time

def contagem_regressiva(segundos):
    print("Inicializando contagem regressiva")

    while segundos > 0:
        print(str(segundos))
        time.sleep(1) # Aguarda 1 segundo antes de imprimir o próximo número
        segundos -= 1
    print("BRUM")

# Exemplo de uso: contagem regressiva de 10 segundos
contagem_regressiva(10)