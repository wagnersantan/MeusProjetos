# Criação de um dicionário chamado 'aluno'
aluno = dict()

# Solicita ao usuário que insira o nome do aluno e armazena no dicionário
aluno['nome'] = str(input('Nome: '))

# Solicita ao usuário que insira a média do aluno e armazena no dicionário
while True:
    try:
        aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
        break  # Sai do loop se a média for inserida corretamente
    except ValueError:
        print("Por favor, insira um número válido para a média.")

# Verifica a situação do aluno com base na média
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'  # Se a média é 7 ou mais, o aluno é aprovado
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'  # Se a média está entre 5 e 7, o aluno está em recuperação
else:
    aluno['situacao'] = 'Reprovado'  # Se a média é menor que 5, o aluno é reprovado

# Exibe uma linha de separação
print('-=' * 30)

# Itera sobre os itens do dicionário e imprime suas chaves e valores
for k, v in aluno.items():
    print(f'{k} é igual a {v}')  # Exibe a chave e o valor correspondente