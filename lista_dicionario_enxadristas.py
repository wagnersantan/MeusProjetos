enxadristas = []  # Criação de uma lista vazia chamada 'enxadristas' para armazenar os enxadristas

while True:
    enxadrista = {}  # Criação de um dicionário para armazenar as informações de cada enxadrista
    enxadrista['nome'] = input('Nome do enxadrista: ')  # Solicita o nome do enxadrista e armazena no dicionário
    tot = int(input(f'Quantas partidas {enxadrista["nome"]} jogou?: '))  # Pergunta quantas partidas o enxadrista jogou

    partidas = []  # Criação de uma lista para armazenar a quantidade de pontos em cada partida
    for c in range(tot):  # Para cada partida que o enxadrista jogou
        partidas.append(int(input(f'Quantos pontos na partida {c + 1}? ')))  # Adiciona o número de pontos à lista 'partidas'

    enxadrista['medalhas'] = partidas  # Armazena a lista 'partidas' no dicionário 'enxadrista'
    enxadrista['Total'] = sum(partidas)  # Calcula a soma dos pontos e armazena no dicionário 'enxadrista'
    
    # Entrada para medalhas
    enxadrista['ouro'] = int(input(f'Quantas medalhas de ouro {enxadrista["nome"]} possui? '))
    enxadrista['prata'] = int(input(f'Quantas medalhas de prata {enxadrista["nome"]} possui? '))
    enxadrista['bronze'] = int(input(f'Quantas medalhas de bronze {enxadrista["nome"]} possui? '))
    
    enxadristas.append(enxadrista)  # Adiciona o dicionário 'enxadrista' à lista 'enxadristas'

    while True:
        resp = input('Deseja cadastrar outro enxadrista? [S/N] ').strip().upper()  # Pergunta se deseja continuar
        if resp in 'SN':  # Verifica se a resposta é válida
            break  # Sai do loop se a resposta for válida
        print('Erro! Responda apenas S ou N:')  # Mensagem de erro se a resposta não for válida

    if resp == 'N':  # Se a resposta for 'N', sai do loop principal
        break

# Função para determinar o enxadrista com mais medalhas
def mais_medalhas(enxadristas):
    max_ouro = max_prata = max_bronze = 0
    campeao_ouro = campeao_prata = campeao_bronze = ''

    for enxadrista in enxadristas:
        if enxadrista['ouro'] > max_ouro:
            max_ouro = enxadrista['ouro']
            campeao_ouro = enxadrista['nome']
        
        if enxadrista['prata'] > max_prata:
            max_prata = enxadrista['prata']
            campeao_prata = enxadrista['nome']
        
        if enxadrista['bronze'] > max_bronze:
            max_bronze = enxadrista['bronze']
            campeao_bronze = enxadrista['nome']

    return campeao_ouro, campeao_prata, campeao_bronze

# Imprimindo resultados
print('-=' * 30)  # Imprime uma linha decorativa
print('cod', end='')  # Imprime 'cod' sem pular linha
for i in enxadristas[0].keys():  # Para cada chave no dicionário do primeiro enxadrista
    print(f'{i:<15}', end='')  # Imprime a chave alinhada à esquerda com um espaço de 15 caracteres
print()  # Pula uma linha
print('-=' * 40)  # Imprime uma linha decorativa

for k, v in enumerate(enxadristas):  # Para cada enxadrista na lista 'enxadristas', com seu índice
    print(f'{k:>3}', end='')  # Imprime o índice do enxadrista alinhado à direita
    for d in v.values():  # Para cada valor no dicionário do enxadrista
        print(f'{str(d):<15}', end='')  # Imprime o valor alinhado à esquerda com um espaço de 15 caracteres
    print()  # Pula uma linha

print('-=' * 40)  # Imprime uma linha decorativa
while True:
    busca = int(input('Mostrar dados de qual enxadrista? (999 para parar): '))  # Pergunta qual enxadrista mostrar
    if busca == 999:  # Se o usuário digitar 999, sai do loop
        break
    if busca >= len(enxadristas):  # Se o código do enxadrista não existir
        print(f'ERRO! Não existe enxadrista com código {busca}')  # Mensagem de erro
    else:
        print(f'--- LEVANTAMENTO DO ENXADRISTAS {enxadristas[busca]["nome"]}')  # Mostra os dados do enxadrista
        print('-=' * 40)  # Linha decorativa

# Mostrando os campeões de medalhas
campeao_ouro, campeao_prata, campeao_bronze = mais_medalhas(enxadristas)
print(f'O enxadrista com mais medalhas de ouro é: {campeao_ouro}')
print(f'O enxadrista com mais medalhas de prata é: {campeao_prata}')
print(f'O enxadrista com mais medalhas de bronze é: {campeao_bronze}')

print('<< Volte sempre >>')  # Mensagem de despedida