from datetime import date
atual = date.today ().year
nascimento = int ((input('Ano de Nascimento:')))
idade = atual - nascimento
print ('O atleta tem {} anos.'.format (idade))
if idade <=9:
    print ('A classificação: Mirin')
elif idade <=14:
    print('Classificação:Junior')
elif idade <=25:
    print ('Classificação: Senior')
else: 
    print('Classificação:Master')

