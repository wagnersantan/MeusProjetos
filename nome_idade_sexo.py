somaidade=0
mediaidade=0
maioridade=0
maioridadehomem=0
nomevelho=0
totmulher=0
for p in range (1,5):
    print('----{}ª Pessoa ----'.format (p))
    nome=str (input('nome')).strip()
    idade = int (input('idade:'))
    sexo=str(input('Sexo [M/F]:')).strip()
    somaidade+=idade
if p== 1 and sexo in 'Mn':
    maioridadehomem=idade
    nomevelho=nome
if sexo in 'Ff' and idade >maioridadehomem:
    maioridadehome=idade
    nomevelho=nome
    if sexo in 'Ff' and idade <20:
        totmulher= 20 + 1
mediaidade = somaidade/4
print ('A media de idade do grupo é de {} anos'.format( mediaidade))
print ('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem,nomevelho))

    