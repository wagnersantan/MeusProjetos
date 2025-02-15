num = int(input('Digite um numero: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:  # Verifica se c é divisor de num
        print('\033[31m{}'.format(c), end=' ')  # Imprime o divisor em vermelho
        tot += 1
    else:
        print('\033[33m{}'.format(c), end=' ')  # Imprime os não divisores em amarelo

print('\033[m O número {} foi divisível {} vezes'.format(num, tot))

if tot == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')