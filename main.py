import os
import random

# Gera um número aleatório de 4 dígitos
numero_aleatorio = random.randint(1000, 9999)

# Define o caminho do ficheiro
pasta = 'tickers'
ficheiro = 'text.txt'
caminho_ficheiro = os.path.join(pasta, ficheiro)

# Verifica se a pasta existe, se não, cria-a
if not os.path.exists(pasta):
    os.makedirs(pasta)

# Abre o ficheiro em modo de adição e escreve o número aleatório
with open(caminho_ficheiro, 'a') as f:
    f.write(f'{numero_aleatorio}\n')

print(f'O número {numero_aleatorio} foi adicionado ao ficheiro {caminho_ficheiro}.')