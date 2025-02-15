# Inicializa uma lista vazia chamada 'ficha' para armazenar os dados dos alunos
ficha = []

# Inicia um loop infinito para coletar dados dos alunos
while True:
    # Solicita o nome do aluno
    nome = str(input('Nome: '))
    
    # Solicita a primeira nota do aluno e converte para float
    nota1 = float(input('Nota 1: '))
    
    # Solicita a segunda nota do aluno e converte para float
    nota2 = float(input('Nota 2: '))
    
    # Calcula a média das duas notas
    media = (nota1 + nota2) / 2
    
    # Adiciona os dados do aluno (nome, notas e média) à lista 'ficha'
    ficha.append([nome, [nota1, nota2], media])
    
    # Pergunta ao usuário se deseja continuar inserindo dados
    resp = str(input('Quer continuar? [S/N]: '))
    
    # Se a resposta for 'N' ou 'n', sai do loop
    if resp in 'Nn':
        break

# Imprime uma linha de separação
print('-=' * 30)
# Exibe o cabeçalho da tabela com nomes, notas e média
print(f'{"Nome":<10}{"Notas":<20}{"Média":>8}')
# Imprime uma linha de separação
print('-' * 60)

# Percorre a lista 'ficha' para exibir os dados de cada aluno
for i, a in enumerate(ficha):
    # Exibe o nome do aluno, suas notas e a média formatada
    print(f'{a[0]:<10}{str(a[1]):<20}{a[2]:>8.1f}')

# Inicia um novo loop para consulta das notas dos alunos
while True:
    # Imprime uma linha de separação
    print('-' * 35)
    # Solicita ao usuário o índice do aluno para mostrar suas notas (999 para sair)
    opc = int(input('Mostrar notas de qual aluno? (999 para interromper): '))
    
    # Se o usuário digitar 999, finaliza o programa
    if opc == 999:
        print('Finalizando...')
        break
    
    # Verifica se o índice fornecido está dentro do intervalo válido
    if 0 <= opc < len(ficha):
        # Exibe as notas do aluno escolhido
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
    else:
        # Informa que o aluno não foi encontrado
        print('Aluno não encontrado. Tente novamente.')

# Mensagem final ao usuário
print('<<<< Volte sempre >>>')