# Inicializando uma lista para armazenar os dados das pessoas
galera = []
soma = 0

while True:
    pessoa = dict()  # Criando um dicionário para armazenar os dados da pessoa
    pessoa['nome'] = str(input('Nome: '))  # Coletando o nome da pessoa

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]  # Coletando o sexo da pessoa
        if pessoa['sexo'] in 'MF':  # Verificando se o sexo é M ou F
            break  # Saindo do loop se o sexo for válido
        print('Erro! Por favor, digite apenas M ou F!')  # Mensagem de erro se o sexo não for válido

    pessoa['idade'] = int(input('Idade: '))  # Coletando a idade da pessoa
    soma += pessoa['idade']  # Acumulando a soma das idades
    galera.append(pessoa.copy())  # Adicionando uma cópia do dicionário pessoa à lista galera

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]  # Perguntando se deseja continuar
        if resp in 'SN':  # Verificando se a resposta é S ou N
            break  # Saindo do loop se a resposta for válida
        print('Erro! Responda apenas S ou N.')  # Mensagem de erro se a resposta não for válida

    if resp == 'N':  # Se a resposta for 'N', sai do loop principal
        break 

print(f'Foram cadastradas {len(galera)} pessoas!')  # Exibindo o número total de pessoas cadastradas
if len(galera) > 0:  # Verificando se há pessoas cadastradas para calcular a média
    media = soma / len(galera)  # Calculando a média de idade
    print(f'A média de idade é de {media:.2f} anos.')  # Exibindo a média de idade

# Exibindo as mulheres cadastradas
print('As mulheres cadastradas foram:', end=' ')
for pessoa in galera:  # Iterando sobre a lista de pessoas
    if pessoa['sexo'] == 'F':  # Verificando se o sexo é feminino
        print(pessoa['nome'], end=' ')  # Exibindo o nome da mulher