somaidade=0
maioridade=0
nomevelho=''
totmulher=0
#solicita ao usúario o número de pessoas 
num_pessoas=int (input('Quantas pessoas você deseja cadastrar?'))
for p in range (1,num_pessoas +1):
    print('----{}ª PESSOA----!.format (p)')
    nome=str (input('nome:')).strip()
    idade=int(input('idade:'))
    sexo=str(input('Sexo [M/F]:')).strip().upper()
    somaidade+=idade
    if p == 1 and sexo=='M':
        maioridadehomem=idade
        nomevelho=nome
    if sexo== 'M'and idade> maioridadehomem:
        maioridadehomem=idade
        nomevelho=nome
    if sexo == 'F'and idade < 20:
        totmulher +=1
# Calcular a media de idade 
    if num_pessoas >0:
        mediaidade=somaidade/num_pessoas 
        print ('A media de idade do grupo é de {:.2f} anos'.format(mediaidade))
    else:
        print('Nenhuma pessoa cadastrada')
    # Exibir informação sobre o homem mais velho
    if maioridadehomem >0:
        print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))
    else:
        
        print('Não foi cadastrado nenhum homem')
    # Exibi o total de mulheres com menos de 20 anos 
        print('Total de mulheres com menos de 20 anos é {}'. foramt(totmulher))