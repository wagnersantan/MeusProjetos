from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' 
[0] Pedra
[1] Papel
[2] Tesoura ''')
print('-=' * 10)

# Adicionando verificação para entrada do jogador
try:
    jogador = int(input('Qual é a sua jogada?'))
    if jogador < 0 or jogador > 2:
        print('Jogada inválida! Escolha um número entre 0 e 2.')
    else:
        print('Jo')
        sleep(1)
        print('Ke')
        sleep(1)
        print('Po!!!')
        print('-=*' * 11)
        print('Computador jogou {}'.format(itens[computador]))
        print('Jogador jogou {}'.format(itens[jogador]))
        print('-=' * 10)

        if computador == jogador:
            print('Empate')
        elif (computador == 0 and jogador == 1) or (computador == 1 and jogador == 2) or (computador == 2 and jogador == 0):
            print('Jogador vence')
        else:
            print('Computador vence')
except ValueError:
    print('Entrada inválida! Por favor, insira um número.')